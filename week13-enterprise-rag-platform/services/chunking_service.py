class ChunkingService:

    def __init__(self, chunk_size=200):

        self.chunk_size = chunk_size

    def chunk_documents(self, documents):

        chunks = []

        for doc in documents:

            text = doc["content"]

            for i in range(0, len(text), self.chunk_size):

                chunk = text[i:i + self.chunk_size]

                chunks.append(
                    {
                        "filename": doc["filename"],
                        "text": chunk
                    }
                )

        return chunks