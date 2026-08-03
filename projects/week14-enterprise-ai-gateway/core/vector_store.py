import faiss
import numpy as np


class EnterpriseVectorStore:

    def __init__(self):

        self.index = None
        self.dimension = None

    def build(self, embeddings):

        embeddings = np.asarray(embeddings, dtype="float32")

        if embeddings.ndim != 2:
            raise ValueError(
                f"Expected 2D embeddings but got shape {embeddings.shape}"
            )

        self.dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(self.dimension)

        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):

        query_embedding = np.asarray(query_embedding, dtype="float32")

        distances, indices = self.index.search(query_embedding, top_k)

        return distances, indices