from sentence_transformers import SentenceTransformer
import numpy as np

from config.settings import EMBEDDING_MODEL


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def encode(self, texts):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return np.asarray(embeddings, dtype="float32")