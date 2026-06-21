from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_results(
    query,
    documents,
    indices,
    top_k=10
):

    pairs = [
        (query, doc)
        for doc in documents
    ]

    scores = reranker.predict(
        pairs
    )

    ranked = sorted(
        zip(indices, documents, scores),
        key=lambda x: x[2],
        reverse=True
    )

    ranked_indices = [
        idx
        for idx, _, _
        in ranked[:top_k]
    ]

    ranked_scores = [
        float(score)
        for _, _, score
        in ranked[:top_k]
    ]

    return (
        ranked_indices,
        ranked_scores
    )