from ingestion.document_loader import EnterpriseDocumentLoader
from services.chunking_service import ChunkingService
from services.context_builder import ContextBuilder
from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSStore
from retriever.retriever import EnterpriseRetriever

loader = EnterpriseDocumentLoader()
documents = loader.load_documents()

chunker = ChunkingService(chunk_size=200)
chunks = chunker.chunk_documents(documents)

embedder = EmbeddingService()

embeddings = embedder.embed_chunks(chunks)

store = FAISSStore()
store.build(embeddings)

retriever = EnterpriseRetriever(store, embedder, chunks)

builder = ContextBuilder()

query = "Explain Retrieval-Augmented Generation"

results = retriever.search(query)

context = builder.build_context(results)

print("\n========================================")
print(" Enterprise RAG Pipeline")
print("========================================")

print("\nUser Question")
print("---------------------------")
print(query)

print("\nRetrieved Context")
print("---------------------------")
print(context)

print("\nPipeline Complete.")