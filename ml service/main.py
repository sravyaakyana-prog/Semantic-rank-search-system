from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

# ==========================
# LOCAL IMPORTS
# ==========================
from src.data_loader import load_dataset

from src.semantic_search import (
    compute_document_embeddings,
    build_faiss_index,
    semantic_search
)

from src.bm25 import BM25Model
from src.reranker import rerank_results

from src.index_manager import load_index, save_index
from src.faiss_index import FaissIndex


# ==========================
# APP SETUP
# ==========================
app = FastAPI(title="SemanticRank API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# LOAD DATASET
# ==========================
print("Loading dataset...")

df = load_dataset()

print("Dataset loaded successfully.")
# ==========================
# FAISS INDEX SETUP
# ==========================
print("Loading FAISS index...")

loaded_index, loaded_embeddings = load_index()

if loaded_index is not None:
    print("✅ Existing FAISS index loaded")

    faiss_index = FaissIndex(loaded_embeddings)
    faiss_index.index = loaded_index

    doc_embeddings = loaded_embeddings

else:
    print("Generating embeddings...")

    doc_embeddings = compute_document_embeddings(df["doc_text"].tolist())

    print("Building FAISS index...")

    faiss_index = build_faiss_index(doc_embeddings)

    print("Saving FAISS index...")

    save_index(faiss_index, doc_embeddings)


# ==========================
# BM25 MODEL
# ==========================
print("Initializing BM25...")
bm25 = BM25Model(df["doc_text"].tolist())


# ==========================
# REQUEST MODEL
# ==========================
class SearchRequest(BaseModel):
    query: str


# ==========================
# ANSWER EXTRACTION
# ==========================
def extract_answer(query, text):
    text = str(text)
    sentences = text.split(".")

    query_words = set(query.lower().split())

    best_sentence = text
    best_score = 0

    for sent in sentences:
        sent_words = set(sent.lower().split())
        overlap = len(query_words.intersection(sent_words))

        if overlap > best_score:
            best_score = overlap
            best_sentence = sent.strip()

    return best_sentence


# ==========================
# ROOT
# ==========================
@app.get("/")
def home():
    return {"message": "SemanticRank API Running"}


# ==========================
# SEARCH API
# ==========================
@app.post("/search")
def search(req: SearchRequest):

    query = req.query

    # STEP 1: SEMANTIC SEARCH
    top_indices, semantic_scores = semantic_search(
        query,
        faiss_index,
        top_k=20
    )

    semantic_scores = np.array(semantic_scores)

    # STEP 2: BM25 SCORES
    bm25_all_scores = bm25.rank(query)

    bm25_scores = np.array([
        float(bm25_all_scores[idx])
        for idx in top_indices
    ])

    # STEP 3: NORMALIZATION
    def minmax(x):
        if np.max(x) == np.min(x):
            return np.zeros_like(x)
        return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-6)

    semantic_scores = minmax(semantic_scores)
    bm25_scores = minmax(bm25_scores)

        # STEP 4: HYBRID RANKING
    alpha = 0.70

    hybrid_scores = (
        alpha * semantic_scores +
        (1 - alpha) * bm25_scores
    )

    ranked = sorted(
        zip(top_indices, hybrid_scores),
        key=lambda x: x[1],
        reverse=True
    )

    ranked_indices = [
        x[0]
        for x in ranked[:10]
    ]

    # STEP 5: RERANKING
    rerank_docs = df.iloc[ranked_indices]["doc_text"].tolist()

    final_indices, rerank_scores = rerank_results(
        query,
        rerank_docs,
        ranked_indices,
        top_k=10
    )

    # STEP 6: FINAL OUTPUT (FIXED INDENTATION)
    final_results = df.iloc[final_indices].copy().reset_index(drop=True)
    final_results["rerank_score"] = rerank_scores

    best_doc = final_results.iloc[0]
    best_answer = extract_answer(query, best_doc["doc_text"])

    available_cols = ["docid", "doc_text", "rerank_score"]

    return {
        "answer": best_answer,
        "results": final_results[available_cols].to_dict(orient="records")
    }

    
    import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )