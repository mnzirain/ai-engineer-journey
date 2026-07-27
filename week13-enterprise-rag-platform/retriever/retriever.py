import numpy as np


class EnterpriseRetriever:

    def __init__(self, faiss_store, embedder, chunks):
        self.store = faiss_store
        self.embedder = embedder
        self.chunks = chunks

    def search(self, query, top_k=3):

        query_embedding = self.embedder.model.encode([query])

        query_embedding = np.array(query_embedding).astype("float32")

        distances, indices = self.store.index.search(query_embedding, top_k)

        results = []

        for idx, distance in zip(indices[0], distances[0]):

            results.append(
                {
                    "filename": self.chunks[idx]["filename"],
                    "text": self.chunks[idx]["text"],
                    "score": float(distance)
                }
            )

        return results