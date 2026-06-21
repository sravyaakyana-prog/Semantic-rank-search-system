import os
import faiss
import numpy as np

INDEX_DIR = "indexes"

INDEX_FILE = os.path.join(
    INDEX_DIR,
    "faiss.index"
)

EMBEDDING_FILE = os.path.join(
    INDEX_DIR,
    "embeddings.npy"
)


def save_index(
    faiss_index,
    embeddings
):
    os.makedirs(
        INDEX_DIR,
        exist_ok=True
    )

    # IMPORTANT
    faiss.write_index(
        faiss_index.index,
        INDEX_FILE
    )

    np.save(
        EMBEDDING_FILE,
        embeddings
    )

    print("✅ FAISS index saved")


def load_index():

    if (
        os.path.exists(INDEX_FILE)
        and
        os.path.exists(EMBEDDING_FILE)
    ):

        index = faiss.read_index(
            INDEX_FILE
        )

        embeddings = np.load(
            EMBEDDING_FILE
        )

        print("✅ FAISS index loaded")

        return index, embeddings

    return None, None