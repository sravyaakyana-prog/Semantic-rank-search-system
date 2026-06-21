from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.data_loader import load_data

from src.semantic_search import (
    compute_document_embeddings,
    build_faiss_index,
    semantic_search
)

from src.bm25 import BM25Model
from src.hybrid_ranker import hybrid_rank
from src.reranker import rerank_results

from src.index_manager import (
    save_index,
    load_index
)

from src.faiss_index import FaissIndex

from src.evaluation import ndcg_at_k

app = FastAPI(title="SemanticRank API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# LOAD DATA
# ==========================================

print("Loading dataset...")

df = load_data()

# ==========================================
# LOAD / BUILD FAISS
# ==========================================

print("Loading FAISS index...")

loaded_index, loaded_embeddings = load_index()

if loaded_index is not None:

    print("✅ Existing FAISS index loaded")

    faiss_index = FaissIndex(
        loaded_embeddings
    )

    faiss_index.index = loaded_index

    doc_embeddings = loaded_embeddings

else:

    print("Generating embeddings...")

    doc_embeddings = compute_document_embeddings(
        df["doc_text"].tolist()
    )

    print("Building FAISS index...")

    faiss_index = build_faiss_index(
        doc_embeddings
    )

    print("Saving FAISS index...")

    save_index(
        faiss_index,
        doc_embeddings
    )

# ==========================================
# BM25
# ==========================================

print("Initializing BM25...")

bm25 = BM25Model(
    df["doc_text"].tolist()
)

# ==========================================
# REQUEST MODEL
# ==========================================

class SearchRequest(BaseModel):
    query: str

# ==========================================
# ANSWER EXTRACTION
# ==========================================

def extract_answer(query, text):

    text = str(text)

    sentences = text.split(".")

    query_words = set(
        query.lower().split()
    )

    best_sentence = text
    best_score = -1

    for sent in sentences:

        sent_words = set(
            sent.lower().split()
        )

        overlap = len(
            query_words.intersection(
                sent_words
            )
        )

        if overlap > best_score:

            best_score = overlap
            best_sentence = sent.strip()

    return best_sentence

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/")
def home():

    return {
        "message": "SemanticRank API Running"
    }

# ==========================================
# SEARCH
# ==========================================

@app.post("/search")
def search(req: SearchRequest):

    query = req.query

    # ======================================
    # STEP 1: FAISS Retrieval
    # ======================================

    top_indices, semantic_scores = semantic_search(
        query,
        faiss_index,
        top_k=20
    )

    semantic_scores = list(
        semantic_scores
    )

    # ======================================
    # STEP 2: BM25 Scores
    # ======================================

    bm25_all_scores = bm25.rank(
        query
    )

    bm25_scores = [
        float(bm25_all_scores[idx])
        for idx in top_indices
    ]

    # ======================================
    # STEP 3: Hybrid Ranking
    # ======================================

    hybrid_scores = hybrid_rank(
        semantic_scores,
        bm25_scores,
        alpha=0.7
    )

    ranked = sorted(
        zip(
            top_indices,
            semantic_scores,
            hybrid_scores
        ),
        key=lambda x: x[2],
        reverse=True
    )

    ranked_indices = [
        x[0]
        for x in ranked[:10]
    ]

    # ======================================
    # STEP 4: CrossEncoder Re-Ranking
    # ======================================

    rerank_docs = [
        df.iloc[idx]["doc_text"]
        for idx in ranked_indices
    ]

    final_indices, rerank_scores = (
        rerank_results(
            query,
            rerank_docs,
            ranked_indices,
            top_k=10
        )
    )

    # ======================================
    # STEP 5: Final Results
    # ======================================

    final_results = (
        df.iloc[final_indices]
        .copy()
        .reset_index(drop=True)
    )

    final_results["rerank_score"] = (
        rerank_scores
    )

    best_doc = final_results.iloc[0]

    best_answer = extract_answer(
        query,
        best_doc["doc_text"]
    )

    # ======================================
    # EVALUATION
    # ======================================

    true_rels = final_results[
        "rel"
    ].values

    ndcg_semantic = ndcg_at_k(
        true_rels,
        final_results[
            "rerank_score"
        ].values,
        k=min(
            10,
            len(final_results)
        )
    )

    bm25_ndcg = 0

    if len(bm25_scores) > 0:

        bm25_rels = [1] * len(
            bm25_scores
        )

        bm25_ndcg = ndcg_at_k(
            bm25_rels,
            bm25_scores,
            k=min(
                10,
                len(bm25_scores)
            )
        )

    improvement = (
        (
            ndcg_semantic
            -
            bm25_ndcg
        )
        /
        (bm25_ndcg + 1e-6)
    ) * 100

    # ======================================
    # RESPONSE
    # ======================================

    return {

        "answer": best_answer,

        "semantic_ndcg": float(
            ndcg_semantic
        ),

        "bm25_ndcg": float(
            bm25_ndcg
        ),

        "improvement": float(
            improvement
        ),

        "results": final_results[
            [
                "docid",
                "doc_text",
                "rerank_score",
                "rel"
            ]
        ].to_dict(
            orient="records"
        )
    }