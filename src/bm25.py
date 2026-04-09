from rank_bm25 import BM25Okapi

class BM25Model:
    def __init__(self, documents):
        self.tokenized_docs = [doc.split() for doc in documents]
        self.model = BM25Okapi(self.tokenized_docs)

    def rank(self, query):
        tokenized_query = query.split()
        scores = self.model.get_scores(tokenized_query)
        return scores