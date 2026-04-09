from src.data_loader import load_data
from src.feature_engineering import create_features
from src.model import train_model
from src.evaluation import ndcg_at_k
from src.bm25 import BM25Model

df = load_data()

# Train on full demo dataset
X, y, qid = create_features(df, fit=True)
model = train_model(X, y, qid)

# Test one query group
query = "cell tower"
subset = df[df["query"] == query].copy()

if len(subset) == 0:
    print("No matching data")
else:
    X_test, y_test, qid_test = create_features(subset, fit=False)
    ml_scores = model.predict(X_test)

    bm25 = BM25Model(subset["doc_text"].tolist())
    bm25_scores = bm25.rank(query)

    ndcg_ml = ndcg_at_k(y_test, ml_scores, k=10)
    ndcg_bm25 = ndcg_at_k(y_test, bm25_scores, k=10)

    print("Query:", query)
    print("ML NDCG@10:", round(ndcg_ml, 4))
    print("BM25 NDCG@10:", round(ndcg_bm25, 4))

    improvement = ((ndcg_ml - ndcg_bm25) / (ndcg_bm25 + 1e-6)) * 100
    print("Improvement over BM25:", round(improvement, 2), "%")