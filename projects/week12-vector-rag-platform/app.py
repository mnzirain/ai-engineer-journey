from ingestion.document_loader import DocumentLoader
from services.chunking_service import ChunkingService
from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSStore
from services.retrieval_service import RetrievalService

print("\n========================================")
print(" Enterprise Semantic Search Platform")
print("========================================")

documents = DocumentLoader.load_documents()

chunks = []

for document in documents:

    chunks.extend(
        ChunkingService.chunk(document["content"])
    )

print(f"\nDocuments Loaded : {len(documents)}")
print(f"Chunks Created   : {len(chunks)}")

print("\nBuilding Embeddings...")

embeddings = EmbeddingService.embed(chunks)

print("Embeddings Created Successfully.")

dimension = len(embeddings[0])

store = FAISSStore(dimension)

store.add(embeddings, chunks)

print("FAISS Vector Store Ready.")

queries = [

    "What is Retrieval-Augmented Generation?",

    "Explain Artificial Intelligence",

    "What are vector databases?"

]

for query in queries:

    print("\n----------------------------------------")
    print("Query:")
    print(query)
    print("----------------------------------------")

    results = RetrievalService.search(query)

    for i, result in enumerate(results, start=1):

        print(f"{i}. {result}")

print("\nEnterprise Semantic Search Complete.")