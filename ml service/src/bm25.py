from rank_bm25 import BM25Okapi
import re
import numpy as np
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download once
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


class BM25Model:

    def __init__(self, documents):

        self.documents = documents

        self.tokenized_docs = [
            self.preprocess(doc)
            for doc in documents
        ]

        self.model = BM25Okapi(self.tokenized_docs)

    def preprocess(self, text):

        text = str(text).lower()

        tokens = re.findall(r"\b[a-z0-9]+\b", text)

        tokens = [
            stemmer.stem(word)
            for word in tokens
            if word not in stop_words
        ]

        return tokens

    def rank(self, query):

        query_tokens = self.preprocess(query)

        scores = self.model.get_scores(query_tokens)

        return np.array(scores)