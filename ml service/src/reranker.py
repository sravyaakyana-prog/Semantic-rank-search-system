# src/reranker.py

def rerank_results(
    query,
    documents,
    indices,
    top_k=10
):
    ranked_indices = indices[:top_k]

    ranked_scores = [
        1.0
        for _ in ranked_indices
    ]

    return (
        ranked_indices,
        ranked_scores
    )