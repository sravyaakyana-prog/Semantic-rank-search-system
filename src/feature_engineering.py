from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

vectorizer = TfidfVectorizer(max_features=500)

def create_features(df, fit=True):
    texts = df["query"].fillna("") + " " + df["doc_text"].fillna("")

    if fit:
        X_tfidf = vectorizer.fit_transform(texts)
    else:
        X_tfidf = vectorizer.transform(texts)

    query_len = df["query"].fillna("").apply(lambda x: len(str(x).split()))
    doc_len = df["doc_text"].fillna("").apply(lambda x: len(str(x).split()))

    X = np.hstack([
        X_tfidf.toarray(),
        query_len.values.reshape(-1, 1),
        doc_len.values.reshape(-1, 1)
    ])

    y = df["rel"].astype(int).values
    qid = df["qid"].values

    return X, y, qid