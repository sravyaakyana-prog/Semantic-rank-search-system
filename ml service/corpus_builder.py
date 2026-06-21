import os
import json
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")


def load_json(file_name, source_name):
    path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return []

    cleaned = []
    for i, doc in enumerate(data):
        text = doc.get("text", "").strip()
        title = doc.get("title", "").strip()

        if len(text) < 20:
            continue

        cleaned.append({
            "id": f"{source_name}_{i}",
            "title": title,
            "text": text,
            "source": source_name
        })

    return cleaned


def load_demo_data():
    """
    Load your relevance dataset (for evaluation later)
    """
    path = os.path.join(DATA_DIR, "demo_data.csv")

    if not os.path.exists(path):
        return pd.DataFrame()

    return pd.read_csv(path)


def build_corpus():
    """
    Main corpus builder
    """

    print("🚀 Building unified corpus...\n")

    wiki = load_json("wikipedia_sample.json", "wikipedia")
    ms = load_json("ms_marco_sample.json", "msmarco")
    custom = load_json("custom_dataset.json", "custom")

    corpus = wiki + ms + custom

    # -------------------------
    # DEDUPLICATION (important)
    # -------------------------
    seen = set()
    unique_corpus = []

    for doc in corpus:
        key = doc["text"][:100].lower()

        if key in seen:
            continue

        seen.add(key)
        unique_corpus.append(doc)

    print(f"📚 Wiki docs: {len(wiki)}")
    print(f"📚 MS MARCO docs: {len(ms)}")
    print(f"📚 Custom docs: {len(custom)}")
    print(f"✅ Final corpus size: {len(unique_corpus)}")

    # Save corpus
    output_path = os.path.join(DATA_DIR, "corpus.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(unique_corpus, f, indent=2)

    print("\n🎉 Corpus saved at:", output_path)

    return unique_corpus


if __name__ == "__main__":
    build_corpus()