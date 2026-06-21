from sentence_transformers import SentenceTransformer
from src.faiss_index import FaissIndex

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def compute_document_embeddings(doc_texts):

    return model.encode(
        doc_texts,
        convert_to_numpy=True
    )


def build_faiss_index(doc_embeddings):

    return FaissIndex(
        doc_embeddings
    )


def semantic_search(
    query,
    faiss_index,
    top_k=10
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    indices, scores = faiss_index.search(
        query_embedding,
        top_k
    )

    return indices, scores