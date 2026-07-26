from memory.memory_store import MemoryStore


class Retriever:
    """
    Enterprise Retrieval Layer

    Retrieves relevant information
    from the shared memory.

    This will later be upgraded to
    a Vector Database Retriever.
    """

    @staticmethod
    def search(query: str):

        memory = MemoryStore.all()

        results = {}

        for key, value in memory.items():

            if query.lower() in key.lower():

                results[key] = value

            elif query.lower() in str(value).lower():

                results[key] = value

        return results