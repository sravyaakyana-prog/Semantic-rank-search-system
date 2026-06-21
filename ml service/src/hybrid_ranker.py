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


def hybrid_rank(
    semantic_scores,
    bm25_scores,
    alpha=0.7
):
    """
    alpha = semantic weight
    1.0 = only semantic
    0.0 = only BM25
    """

    semantic_scores = minmax_normalize(
        semantic_scores
    )

    bm25_scores = minmax_normalize(
        bm25_scores
    )

    hybrid_scores = (
        alpha * semantic_scores
        +
        (1 - alpha) * bm25_scores
    )

    return hybrid_scores