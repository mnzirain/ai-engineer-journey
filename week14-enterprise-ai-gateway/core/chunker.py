class SmartChunker:

    def __init__(self, chunk_size=250):

        self.chunk_size = chunk_size

    def split(self, documents):

        chunks = []

        for document in documents:

            text = document["text"]

            for i in range(0, len(text), self.chunk_size):

                piece = text[i:i+self.chunk_size].strip()

                if piece:

                    chunks.append(
                        {
                            "source": document["source"],
                            "text": piece
                        }
                    )

        return chunks