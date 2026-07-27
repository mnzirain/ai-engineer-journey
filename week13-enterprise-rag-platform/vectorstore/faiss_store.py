import faiss
import numpy as np


class FAISSStore:

    def __init__(self):

        self.index = None

    def build(self, embeddings):

        embeddings = np.array(embeddings).astype("float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        return self.index