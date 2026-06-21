import xgboost as xgb
import numpy as np

def train_model(X, y, qid):
    # Only convert y (qid already numpy)
    if hasattr(y, "values"):
        y = y.values

    order = np.argsort(qid)

    X = X[order]
    y = y[order]
    qid = qid[order]

    _, group = np.unique(qid, return_counts=True)

    model = xgb.XGBRanker(
        objective='rank:pairwise',
        learning_rate=0.1,
        n_estimators=50,
        max_depth=6
    )

    model.fit(X, y, group=group)

    return model
