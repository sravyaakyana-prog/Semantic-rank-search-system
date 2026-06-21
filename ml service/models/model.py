from sentence_transformers import SentenceTransformer
import numpy as np


class SBERTModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Lightweight, fast, production-safe embedding model
        """

        print("🔄 Loading SBERT model...")
        self.model = SentenceTransformer(model_name)
        print("✅ SBERT loaded")

        self.embeddings = None
        self.documents = None

    # -----------------------------
    # BUILD EMBEDDINGS
    # -----------------------------
    def build(self, documents):
        """
        documents: list of dicts (your corpus)
        """

        self.documents = documents

        texts = [
            doc["title"] + " " + doc["text"]
            for doc in documents
        ]

        print("🔄 Creating embeddings...")
        self.embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        print("✅ Embeddings ready")

    # -----------------------------
    # SEARCH
    # -----------------------------
    def search(self, query, top_k=5):
        """
        Semantic search using cosine similarity
        """

        query_vec = self.model.encode(
            [query],
            convert_to_numpy=True
        )[0]

        # cosine similarity
        scores = np.dot(self.embeddings, query_vec) / (
            np.linalg.norm(self.embeddings, axis=1) *
            np.linalg.norm(query_vec) + 1e-9
        )

        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []

        for idx in top_indices:
            doc = self.documents[idx]

            results.append({
                "id": doc["id"],
                "title": doc["title"],
                "text": doc["text"],
                "source": doc["source"],
                "score": float(scores[idx])
            })

        return results