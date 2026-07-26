import faiss
import numpy as np


class FAISSStore:
    """
    Enterprise FAISS Vector Store
    """

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)

        self.documents = []

    def add(self, embeddings, texts):

        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.documents.extend(texts)

    def search(self, embedding, top_k=3):

        embedding = np.array([embedding]).astype("float32")

        distances, indices = self.index.search(embedding, top_k)

        results = []

        for idx in indices[0]:

            if idx < len(self.documents):

                results.append(self.documents[idx])

        return results