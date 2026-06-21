from sentence_transformers import SentenceTransformer
import numpy as np
from src.faiss_index import FaissIndex

# ==========================
# MODEL (KEEP SAME)
# ==========================

model = SentenceTransformer("all-MiniLM-L6-v2")


# ==========================
# EMBEDDINGS (FIXED)
# ==========================

def compute_document_embeddings(doc_texts):

    embeddings = model.encode(
        doc_texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        batch_size=32,
        show_progress_bar=True 
    )

    return embeddings


# ==========================
# FAISS BUILD
# ==========================

def build_faiss_index(doc_embeddings):

    return FaissIndex(doc_embeddings)


# ==========================
# SEMANTIC SEARCH (FIXED)
# ==========================

def semantic_search(query, faiss_index, top_k=10):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True   # 🔥 CRITICAL FIX
    )

    indices, scores = faiss_index.search(
        query_embedding,
        top_k
    )

    return indices, scores