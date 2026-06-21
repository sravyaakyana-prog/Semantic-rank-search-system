import pandas as pd
import json
import os

def load_dataset():
    base_path = os.path.join("data", "scifact")

    corpus_file = os.path.join(base_path, "corpus.json")

    # BEIR corpus format
    with open(corpus_file, "r", encoding="utf-8") as f:
        corpus = json.load(f)

    docs = []
    for doc_id, doc in corpus.items():
        docs.append({
            "docid": doc_id,
            "doc_text": doc.get("text", "")
        })

    df = pd.DataFrame(docs)

    print("📂 Dataset loaded locally:", len(df), "docs")
    return df