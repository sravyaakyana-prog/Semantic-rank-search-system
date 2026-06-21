import faiss
import numpy as np


class FaissIndex:

    def __init__(self, embeddings):

        self.embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = self.embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        faiss.normalize_L2(
            self.embeddings
        )

        self.index.add(
            self.embeddings
        )

    def search(
        self,
        query_embedding,
        top_k=10
    ):

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        faiss.normalize_L2(
            query_embedding
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        return (
            indices[0],
            scores[0]
        )