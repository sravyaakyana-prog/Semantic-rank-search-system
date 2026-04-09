import streamlit as st
from src.data_loader import load_data
from src.semantic_search import compute_document_embeddings, semantic_search
from src.bm25 import BM25Model
from src.evaluation import ndcg_at_k

st.set_page_config(
    page_title="Semantic Search & Answer System",
    page_icon="🔎",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}
.subtitle {
    font-size: 1.05rem;
    color: #b0b0b0;
    margin-bottom: 1.5rem;
}
.section-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-top: 1.2rem;
    margin-bottom: 0.8rem;
}
.answer-box {
    background-color: #123d26;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #1f6f46;
    font-size: 1.15rem;
    font-weight: 500;
}
.result-card {
    background-color: #111827;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #2d3748;
    margin-bottom: 14px;
}
.result-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 0.4rem;
}
.result-text {
    color: #d1d5db;
    margin-bottom: 0.5rem;
}
.small-label {
    color: #9ca3af;
    font-size: 0.92rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔎 SemanticRank: Intelligent Search & Answer System</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Understands the meaning of user queries using sentence embeddings, retrieves the most relevant documents, extracts the best answer, and compares against a BM25 baseline.</div>',
    unsafe_allow_html=True
)

st.caption("Try: cell tower | mobile signal | machine learning | birds raised | internet")
query_input = st.text_input("Enter your question:")

@st.cache_data
def load_all():
    return load_data()

df = load_all()

@st.cache_resource
def get_embeddings(df):
    doc_embeddings = compute_document_embeddings(df["doc_text"].tolist())
    return doc_embeddings

doc_embeddings = get_embeddings(df)

def extract_answer(query, text):
    text = str(text)
    sentences = text.split(".")
    query_words = set(query.lower().split())

    best_sentence = text
    best_score = -1

    for sent in sentences:
        sent_words = set(sent.lower().split())
        overlap = len(query_words.intersection(sent_words))
        if overlap > best_score:
            best_score = overlap
            best_sentence = sent.strip()

    return best_sentence

if query_input:
    st.markdown('<div class="section-title">📌 Results</div>', unsafe_allow_html=True)

    top_indices, semantic_scores = semantic_search(
        query_input,
        df["doc_text"].tolist(),
        doc_embeddings,
        top_k=10
    )

    top_results = df.iloc[top_indices].copy()
    top_results["semantic_score"] = semantic_scores

    best_doc = top_results.iloc[0]
    best_answer = extract_answer(query_input, best_doc["doc_text"])

    left, right = st.columns([1.6, 1])

    with left:
        st.markdown('<div class="section-title">💡 Best Answer</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="answer-box">{best_answer}</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="section-title">📊 Evaluation</div>', unsafe_allow_html=True)

        # BM25 baseline
        bm25 = BM25Model(df["doc_text"].tolist())
        bm25_scores = bm25.rank(query_input)

        # Semantic relevance used as pseudo-score
        true_rels = top_results["rel"].values

        ndcg_semantic = ndcg_at_k(true_rels, top_results["semantic_score"].values, k=10)
        ndcg_bm25 = ndcg_at_k(df["rel"].values, bm25_scores, k=10)
        improvement = ((ndcg_semantic - ndcg_bm25) / (ndcg_bm25 + 1e-6)) * 100

        c1, c2, c3 = st.columns(3)
        c1.metric("Semantic NDCG@10", round(float(ndcg_semantic), 4))
        c2.metric("BM25 NDCG@10", round(float(ndcg_bm25), 4))
        c3.metric("Improvement", f"{round(float(improvement), 2)}%")

    st.markdown("---")
    st.markdown('<div class="section-title">📚 Top Supporting Results</div>', unsafe_allow_html=True)

    for rank, (_, row) in enumerate(top_results.iterrows(), start=1):
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">🏆 Rank #{rank} — {row['docid']}</div>
            <div class="result-text">{row['doc_text']}</div>
            <div class="small-label">🧠 Semantic Score: {round(float(row['semantic_score']), 4)} &nbsp;&nbsp; | &nbsp;&nbsp; ⭐ Relevance: {row['rel']}</div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Enter a question to see semantic search results, best answer, and evaluation metrics.")