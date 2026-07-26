from ingestion.document_loader import DocumentLoader
from services.chunking_service import ChunkingService

from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSStore


class RetrievalService:
    """
    Enterprise Semantic Retrieval Service
    """

    documents = DocumentLoader.load_documents()

    chunks = []

    for document in documents:
        chunks.extend(
            ChunkingService.chunk(document["content"])
        )

    embeddings = EmbeddingService.embed(chunks)

    dimension = len(embeddings[0])

    store = FAISSStore(dimension)

    store.add(embeddings, chunks)

    @classmethod
    def search(cls, query):

        query_embedding = EmbeddingService.embed([query])[0]

        return cls.store.search(query_embedding)