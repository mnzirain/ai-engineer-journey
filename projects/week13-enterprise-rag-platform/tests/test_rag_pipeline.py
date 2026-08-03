from ingestion.document_loader import EnterpriseDocumentLoader
from services.chunking_service import ChunkingService
from services.context_builder import ContextBuilder
from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSStore
from retriever.retriever import EnterpriseRetriever


def test_enterprise_rag_pipeline():

    loader = EnterpriseDocumentLoader()
    documents = loader.load_documents()

    assert len(documents) > 0

    chunker = ChunkingService(chunk_size=200)
    chunks = chunker.chunk_documents(documents)

    assert len(chunks) > 0

    embedder = EmbeddingService()

    embeddings = embedder.embed_chunks(chunks)

    assert len(embeddings) == len(chunks)

    store = FAISSStore()

    store.build(embeddings)

    retriever = EnterpriseRetriever(
        store,
        embedder,
        chunks
    )

    results = retriever.search(
        "Artificial Intelligence"
    )

    assert len(results) > 0

    builder = ContextBuilder()

    context = builder.build_context(results)

    assert len(context) > 0

    assert "Source:" in context