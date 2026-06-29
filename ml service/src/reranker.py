def rerank_results(query, documents, indices, top_k=10):
    if not documents:
        return [], []

    final_indices = indices[:top_k]

    final_scores = [
        1.0 - (i * 0.03)
        for i in range(len(final_indices))
    ]

    return final_indices, final_scores