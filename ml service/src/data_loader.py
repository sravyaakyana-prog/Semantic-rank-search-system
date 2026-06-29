import pandas as pd
import json
import os
import csv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "scifact")


def load_dataset():
    corpus_jsonl = os.path.join(DATA_DIR, "corpus.jsonl")
    corpus_json = os.path.join(DATA_DIR, "corpus.json")

    docs = []

    if os.path.exists(corpus_jsonl):
        with open(corpus_jsonl, "r", encoding="utf-8") as f:
            for line in f:
                doc = json.loads(line)

                doc_id = str(doc.get("_id", ""))
                title = doc.get("title", "")
                text = doc.get("text", "")

                docs.append({
                    "docid": doc_id,
                    "title": title,
                    "doc_text": (title + " " + text).strip()
                })

    elif os.path.exists(corpus_json):
        with open(corpus_json, "r", encoding="utf-8") as f:
            corpus = json.load(f)

        for doc_id, doc in corpus.items():
            title = doc.get("title", "")
            text = doc.get("text", "")

            docs.append({
                "docid": str(doc_id),
                "title": title,
                "doc_text": (title + " " + text).strip()
            })

    else:
        raise FileNotFoundError("No corpus.jsonl or corpus.json found")

    df = pd.DataFrame(docs)

    print("Dataset loaded:", len(df), "docs")

    return df


def load_queries():
    queries_file = os.path.join(DATA_DIR, "queries.jsonl")

    queries = {}

    if not os.path.exists(queries_file):
        return queries

    with open(queries_file, "r", encoding="utf-8") as f:
        for line in f:
            q = json.loads(line)
            queries[str(q["_id"])] = q["text"]

    return queries


def load_qrels(split="test"):
    qrels_file = os.path.join(DATA_DIR, "qrels", f"{split}.tsv")

    qrels = {}

    if not os.path.exists(qrels_file):
        return qrels

    with open(qrels_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")

        for row in reader:
            qid = str(row.get("query-id") or row.get("qid"))
            docid = str(row.get("corpus-id") or row.get("docid"))
            score = int(row.get("score") or row.get("rel") or 0)

            qrels.setdefault(qid, {})
            qrels[qid][docid] = score

    return qrels