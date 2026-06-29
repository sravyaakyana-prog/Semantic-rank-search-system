import numpy as np
from sentence_transformers import CrossEncoder


_reranker = None


def get_reranker():
    global _reranker

    if _reranker is None:
        print("Loading CrossEncoder reranker...")
        _reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
        print("CrossEncoder loaded")

    return _reranker


def rerank_results(query, documents, indices, top_k=10):
    if len(documents) == 0:
        return [], []

    try:
        model = get_reranker()

        pairs = [
            [query, doc]
            for doc in documents
        ]

        scores = model.predict(pairs)

        order = np.argsort(scores)[::-1][:top_k]

        final_indices = [
            indices[i]
            for i in order
        ]

        final_scores = [
            float(scores[i])
            for i in order
        ]

        return final_indices, final_scores

    except Exception as e:
        print("Reranker failed, fallback used:", e)

        fallback_indices = indices[:top_k]
        fallback_scores = [1.0 for _ in fallback_indices]

        return fallback_indices, fallback_scores