from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Enterprise Embedding Service

    Generates vector embeddings for text.
    """

    model = SentenceTransformer("all-MiniLM-L6-v2")

    @classmethod
    def embed(cls, texts):

        return cls.model.encode(texts, convert_to_numpy=True)