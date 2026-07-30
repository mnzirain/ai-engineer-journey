from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class SearchService:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.documents = []

        self.sources = []

        data_folder = Path("data")

        for file in data_folder.glob("*.txt"):

            text = file.read_text(encoding="utf-8")

            chunks = text.split("\n\n")

            for chunk in chunks:

                chunk = chunk.strip()

                if chunk:

                    self.documents.append(chunk)

                    self.sources.append(file.name)

        embeddings = self.model.encode(self.documents)

        embeddings = np.array(embeddings).astype("float32")

        self.index = faiss.IndexFlatL2(embeddings.shape[1])

        self.index.add(embeddings)

    def search(self, query):

        query_embedding = self.model.encode([query])

        query_embedding = np.array(query_embedding).astype("float32")

        _, indices = self.index.search(query_embedding, 3)

        results = []

        for idx in indices[0]:

            results.append({

                "source": self.sources[idx],

                "text": self.documents[idx]

            })

        return results