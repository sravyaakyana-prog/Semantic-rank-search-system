from beir import util
from beir.datasets.data_loader import GenericDataLoader
import pandas as pd
import os

def load_dataset():
    dataset = "scifact"
    url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset}.zip"

    data_path = util.download_and_unzip(url, "data")
    print("📂 Dataset loaded at:", data_path)

    corpus, queries, qrels = GenericDataLoader(data_path).load(split="test")

    # convert corpus → dataframe
    docs = []
    for doc_id, doc in corpus.items():
        docs.append({
            "docid": doc_id,
            "doc_text": doc["text"]
        })

    df = pd.DataFrame(docs)
    return df