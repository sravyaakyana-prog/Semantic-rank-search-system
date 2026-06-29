import numpy as np


def dcg(relevances):
    relevances = np.array(relevances)
    return np.sum(
        relevances / np.log2(np.arange(len(relevances)) + 2)
    )


def ndcg_at_k(true_rels, pred_scores, k=10):
    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    if len(true_rels) == 0:
        return 0.0

    k = min(k, len(true_rels))

    order = np.argsort(pred_scores)[::-1][:k]
    sorted_rels = true_rels[order]

    dcg_val = dcg(sorted_rels)

    ideal_rels = np.sort(true_rels)[::-1][:k]
    idcg = dcg(ideal_rels)

    if idcg == 0:
        return 0.0

    return float(dcg_val / idcg)


def precision_at_k(true_rels, pred_scores, k=10):
    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    if len(true_rels) == 0:
        return 0.0

    k = min(k, len(true_rels))

    order = np.argsort(pred_scores)[::-1][:k]
    rel = true_rels[order]

    return float(np.sum(rel > 0) / k)


def recall_at_k(true_rels, pred_scores, k=10):
    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    total_rel = np.sum(true_rels > 0)

    if total_rel == 0:
        return 0.0

    k = min(k, len(true_rels))

    order = np.argsort(pred_scores)[::-1][:k]
    rel = true_rels[order]

    return float(np.sum(rel > 0) / total_rel)


def mrr(true_rels, pred_scores):
    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    order = np.argsort(pred_scores)[::-1]
    rel = true_rels[order]

    for i, r in enumerate(rel):
        if r > 0:
            return float(1 / (i + 1))

    return 0.0


def average_precision(true_rels, pred_scores):
    true_rels = np.array(true_rels)
    pred_scores = np.array(pred_scores)

    order = np.argsort(pred_scores)[::-1]
    rel = true_rels[order]

    hits = 0
    precisions = []

    for i, r in enumerate(rel):
        if r > 0:
            hits += 1
            precisions.append(hits / (i + 1))

    if len(precisions) == 0:
        return 0.0

    return float(np.mean(precisions))