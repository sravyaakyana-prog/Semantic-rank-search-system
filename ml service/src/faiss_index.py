import faiss
import numpy as np


class FaissIndex:

    def __init__(self, embeddings):

        # Convert + normalize FIRST (clean pipeline)
        self.embeddings = np.array(embeddings, dtype="float32")
        faiss.normalize_L2(self.embeddings)

        dimension = self.embeddings.shape[1]

        # cosine similarity via inner product
        self.index = faiss.IndexFlatIP(dimension)

        # add normalized vectors
        self.index.add(self.embeddings)

    def search(self, query_embedding, top_k=10):

        query_embedding = np.array(query_embedding, dtype="float32")
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)

        return indices[0], scores[0]