import numpy as np


def minmax_normalize(scores):

    scores = np.array(scores)

    if scores.max() == scores.min():
        return np.ones_like(scores)

    return (
        scores - scores.min()
    ) / (
        scores.max() - scores.min()
    )


def get_alpha(query):

    words = len(query.split())

    if words <= 2:
        return 0.40

    elif words <= 5:
        return 0.60

    else:
        return 0.80


def hybrid_rank(
    query,
    semantic_scores,
    bm25_scores
):

    semantic_scores = minmax_normalize(
        semantic_scores
    )

    bm25_scores = minmax_normalize(
        bm25_scores
    )

    alpha = get_alpha(query)

    hybrid_scores = (
        alpha * semantic_scores
        +
        (1 - alpha) * bm25_scores
    )

    return hybrid_scores