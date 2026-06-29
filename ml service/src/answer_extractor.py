import re
import numpy as np


def normalize_score(value, max_value):
    if max_value == 0:
        return 0
    return value / max_value


def extract_answer(query, documents, max_sentences=2):
    """
    Extract best answer snippet from top retrieved documents.
    """

    query_words = set(
        re.findall(r"\w+", query.lower())
    )

    candidates = []

    for doc in documents[:3]:
        doc = str(doc)

        sentences = re.split(r"(?<=[.!?])\s+", doc)

        for sentence in sentences:
            sentence = sentence.strip()

            if len(sentence) < 30:
                continue

            words = set(
                re.findall(r"\w+", sentence.lower())
            )

            if not words:
                continue

            overlap = len(query_words.intersection(words))

            overlap_score = normalize_score(
                overlap,
                len(query_words)
            )

            length_penalty = 1 / (1 + abs(len(words) - 25) / 25)

            final_score = (
                0.75 * overlap_score
                + 0.25 * length_penalty
            )

            candidates.append(
                (sentence, final_score)
            )

    if not candidates:
        return str(documents[0])[:300] if documents else ""

    candidates = sorted(
        candidates,
        key=lambda x: x[1],
        reverse=True
    )

    best_sentences = [
        sent for sent, score in candidates[:max_sentences]
    ]

    return " ".join(best_sentences)