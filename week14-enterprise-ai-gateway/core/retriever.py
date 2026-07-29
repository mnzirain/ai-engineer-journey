from config.settings import TOP_K


class EnterpriseRetriever:

    def __init__(self, vector_store, embedding_service, chunks):

        self.vector_store = vector_store
        self.embedding_service = embedding_service
        self.chunks = chunks

    def search(self, query):

        query_embedding = self.embedding_service.encode([query])

        distances, indices = self.vector_store.search(
            query_embedding,
            TOP_K
        )

        results = []

        for idx in indices[0]:

            results.append(self.chunks[idx])

        return results