from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_document_embeddings(doc_texts):
    return model.encode(doc_texts, convert_to_numpy=True)

def semantic_search(query, doc_texts, doc_embeddings, top_k=10):
    query_embedding = model.encode([query], convert_to_numpy=True)
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

    top_indices = np.argsort(similarities)[::-1][:top_k]
    top_scores = similarities[top_indices]

    return top_indices, top_scores