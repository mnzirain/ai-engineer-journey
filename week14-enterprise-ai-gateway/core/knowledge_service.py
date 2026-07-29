from config.settings import DATA_DIR

from core.document_loader import DocumentLoader
from core.chunker import SmartChunker
from core.embedding_service import EmbeddingService
from core.vector_store import EnterpriseVectorStore
from core.retriever import EnterpriseRetriever


class KnowledgeService:

    def __init__(self):

        loader = DocumentLoader(DATA_DIR)

        documents = loader.load()

        chunker = SmartChunker()

        chunks = chunker.split(documents)

        embedding_service = EmbeddingService()

        embeddings = embedding_service.encode(
            [chunk["text"] for chunk in chunks]
        )

        vector_store = EnterpriseVectorStore()

        vector_store.build(embeddings)

        self.documents = documents
        self.chunks = chunks
        self.embedding_service = embedding_service
        self.vector_store = vector_store

        self.retriever = EnterpriseRetriever(
            vector_store,
            embedding_service,
            chunks
        )

    def search(self, query):

        return self.retriever.search(query)

    def stats(self):

        return {
            "documents": len(self.documents),
            "chunks": len(self.chunks)
        }