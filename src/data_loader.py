import pandas as pd

def load_data():
    df = pd.read_csv("data/demo_data.csv")
    return df[["qid", "query", "docid", "doc_text", "rel"]]