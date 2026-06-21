import numpy as np


def dcg(relevances):
    """
    Discounted Cumulative Gain
    """
    relevances = np.array(relevances)

    return np.sum(
        relevances / np.log2(np.arange(len(relevances)) + 2)
    )


def ndcg_at_k(true_rels, pred_scores, k=10):
    """
    Normalized Discounted Cumulative Gain @ K

    true_rels: ground truth relevance scores
    pred_scores: model predicted scores (BM25 / SBERT / hybrid)
    """

    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    if len(true_rels) == 0:
        return 0.0

    # sort by predicted score (descending)
    order = np.argsort(pred_scores)[::-1]

    sorted_rels = true_rels[order][:k]

    dcg_val = dcg(sorted_rels)

    # ideal ranking
    ideal_rels = np.sort(true_rels)[::-1][:k]
    idcg = dcg(ideal_rels)

    if idcg == 0:
        return 0.0

    return dcg_val / idcg