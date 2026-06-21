from datasets import load_dataset
import json
import os

# -----------------------------
# PATH SETUP
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(DATA_DIR, exist_ok=True)

print("🚀 Starting dataset build...\n")

# -----------------------------
# 1. WIKITEXT (Wikipedia replacement - stable)
# -----------------------------
print("📚 Loading WikiText dataset...")

try:
    wiki = load_dataset("wikitext", "wikitext-2-raw-v1", split="train[:2%]")

    wiki_data = []
    for item in wiki:
        text = item["text"].strip()

        # skip empty/noisy lines
        if len(text) < 30:
            continue

        wiki_data.append({
            "title": "WikiText Document",
            "text": text[:1000]
        })

    with open(os.path.join(DATA_DIR, "wikipedia_sample.json"), "w", encoding="utf-8") as f:
        json.dump(wiki_data, f, indent=2)

    print(f"✅ WikiText saved: {len(wiki_data)} docs\n")

except Exception as e:
    print("❌ WikiText failed:", str(e))
    wiki_data = []

# -----------------------------
# 2. MS MARCO (Search dataset)
# -----------------------------
print("❓ Loading MS MARCO dataset...")

try:
    msmarco = load_dataset("ms_marco", "v1.1", split="validation[:1%]")

    ms_data = []

    for item in msmarco:
        try:
            ms_data.append({
                "title": item["query"],
                "text": item["passages"]["passage_text"][0]
            })
        except:
            continue

    with open(os.path.join(DATA_DIR, "ms_marco_sample.json"), "w", encoding="utf-8") as f:
        json.dump(ms_data, f, indent=2)

    print(f"✅ MS MARCO saved: {len(ms_data)} docs\n")

except Exception as e:
    print("❌ MS MARCO failed:", str(e))
    ms_data = []

# -----------------------------
# 3. CUSTOM DATASET (Your domain layer)
# -----------------------------
print("🧪 Creating custom dataset...")

custom_data = [
    {
        "title": "Semantic Search Explained",
        "text": "Semantic search improves retrieval by understanding meaning using embeddings instead of keywords."
    },
    {
        "title": "What is BM25",
        "text": "BM25 is a ranking algorithm used in information retrieval systems to score document relevance."
    },
    {
        "title": "Hybrid Search",
        "text": "Hybrid search combines BM25 keyword search with vector embeddings for better ranking accuracy."
    },
    {
        "title": "Sentence Transformers",
        "text": "Sentence Transformers convert text into dense vector embeddings for semantic similarity search."
    },
    {
        "title": "Vector Databases",
        "text": "Vector databases store embeddings and allow fast similarity search over high-dimensional data."
    }
]

with open(os.path.join(DATA_DIR, "custom_dataset.json"), "w", encoding="utf-8") as f:
    json.dump(custom_data, f, indent=2)

print(f"✅ Custom dataset saved: {len(custom_data)} docs\n")

# -----------------------------
# FINAL SUMMARY
# -----------------------------
total = len(wiki_data) + len(ms_data) + len(custom_data)

print("===================================")
print("🎉 DATASET BUILD COMPLETE")
print(f"📊 Total documents: {total}")
print(f"📁 Saved in: {DATA_DIR}")
print("===================================")