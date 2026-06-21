from datasets import load_dataset

def load_msmarco():
    dataset = load_dataset("ms_marco", "v1.1", split="train[:2000]")

    docs = []

    for i, item in enumerate(dataset):
        passage = item.get("passages", {}).get("passage_text", [])

        if isinstance(passage, list):
            text = " ".join(passage)
        else:
            text = str(passage)

        docs.append({
            "id": str(i),
            "title": item.get("query", ""),
            "text": text,
            "source": "msmarco"
        })

    return docs