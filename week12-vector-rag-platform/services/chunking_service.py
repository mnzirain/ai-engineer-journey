class ChunkingService:
    """
    Enterprise Smart Chunking Service

    Splits text into chunks without
    breaking words.
    """

    @staticmethod
    def chunk(text, chunk_size=120):

        words = text.split()

        chunks = []

        current_chunk = ""

        for word in words:

            if len(current_chunk) + len(word) + 1 <= chunk_size:

                current_chunk += word + " "

            else:

                chunks.append(current_chunk.strip())

                current_chunk = word + " "

        if current_chunk:

            chunks.append(current_chunk.strip())

        return chunks