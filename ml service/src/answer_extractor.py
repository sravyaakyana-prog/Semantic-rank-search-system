from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def extract_answer(
    query,
    document_text
):

    document_text = str(
        document_text
    )

    sentences = [
        s.strip()
        for s in document_text.split(".")
        if s.strip()
    ]

    if len(sentences) == 0:
        return document_text

    query_embedding = model.encode(
        [query]
    )

    sentence_embeddings = model.encode(
        sentences
    )

    similarities = cosine_similarity(
        query_embedding,
        sentence_embeddings
    )[0]

    best_idx = similarities.argmax()

    return sentences[best_idx]