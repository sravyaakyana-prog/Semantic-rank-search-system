from rank_bm25 import BM25Okapi
import re
import numpy as np


class BM25Model:

    def __init__(self, documents):

        self.documents = documents

        self.tokenized_docs = [
            self.tokenize(doc)
            for doc in documents
        ]

        self.model = BM25Okapi(
            self.tokenized_docs
        )

    def tokenize(self, text):

        text = str(text).lower()

        return re.findall(
            r"\w+",
            text
        )

    def rank(self, query):

        tokenized_query = self.tokenize(
            query
        )

        scores = self.model.get_scores(
            tokenized_query
        )

        return np.array(scores)