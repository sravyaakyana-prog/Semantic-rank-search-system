
import os
import json
import pandas as pd
from typing import List, Dict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(
    BASE_DIR,
    "data",
    "raw"
)
print("DATA_DIR =", DATA_DIR)

WIKI_FILE = os.path.join(DATA_DIR, "wikipedia_sample.json")
MSMARCO_FILE = os.path.join(DATA_DIR, "ms_marco_sample.json")
CUSTOM_FILE = os.path.join(DATA_DIR, "custom_dataset.json")


def load_json(file_path: str):
    """Safely load JSON file"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except:
        return []


def normalize(doc: Dict, source: str, idx: int):
    """
    Convert any dataset format → unified format
    """

    return {
        "id": f"{source}_{idx}",
        "title": doc.get("title", "").strip(),
        "text": doc.get("text", "").strip(),
        "source": source
    }


def generate_fallback_dataset() -> List[Dict]:
    """
    Since your datasets are empty,
    we create a minimal working corpus for testing pipeline
    """

    fallback_docs = [
        {
            "title": "What is Machine Learning",
            "text": "Machine learning is a branch of artificial intelligence that enables systems to learn patterns from data without explicit programming.",
        },
        {
            "title": "Deep Learning Overview",
            "text": "Deep learning uses neural networks with multiple layers to model complex patterns in data.",
        },
        {
            "title": "Information Retrieval",
            "text": "Information retrieval deals with obtaining relevant information from large datasets such as search engines.",
        },
        {
            "title": "BM25 Algorithm",
            "text": "BM25 is a ranking function used by search engines to estimate relevance of documents to a query.",
        },
        {
            "title": "Sentence Transformers",
            "text": "Sentence transformers convert sentences into dense vector embeddings for semantic search tasks.",
        }
    ]

    return [normalize(doc, "fallback", i) for i, doc in enumerate(fallback_docs)]


def load_all_datasets() -> List[Dict]:
    """
    Main loader:
    - loads all datasets
    - handles empty files
    - falls back if needed
    """

    wiki = load_json(WIKI_FILE)
    ms = load_json(MSMARCO_FILE)
    custom = load_json(CUSTOM_FILE)

    all_docs = []

    for i, d in enumerate(wiki):
        all_docs.append(normalize(d, "wikipedia", i))

    for i, d in enumerate(ms):
        all_docs.append(normalize(d, "msmarco", i))

    for i, d in enumerate(custom):
        all_docs.append(normalize(d, "custom", i))

    # 🧠 fallback if everything is empty
    if len(all_docs) == 0:
        print("⚠️ No datasets found — using fallback corpus")
        all_docs = generate_fallback_dataset()

    print(f"✅ Loaded {len(all_docs)} documents")

    return all_docs

    import pandas as pd


def load_data():
    """
    Converts corpus into DataFrame format expected by main.py
    """

    docs = load_all_datasets()

    rows = []

    for i, doc in enumerate(docs):
        rows.append({
            "qid": i + 1,
            "query": doc["title"],
            "docid": doc["id"],
            "doc_text": doc["text"],
            "rel": 1
        })

    return pd.DataFrame(rows)