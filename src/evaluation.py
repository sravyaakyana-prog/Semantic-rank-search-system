import numpy as np

def dcg(relevances):
    return sum([
        rel / np.log2(idx + 2)
        for idx, rel in enumerate(relevances)
    ])

def ndcg_at_k(true_rels, pred_scores, k=10):
    order = np.argsort(pred_scores)[::-1]
    sorted_rels = np.array(true_rels)[order][:k]

    dcg_val = dcg(sorted_rels)

    ideal_rels = sorted(true_rels, reverse=True)[:k]
    idcg = dcg(ideal_rels)

    if idcg == 0:
        return 0

    return dcg_val / idcg