from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

import faiss
import numpy as np


class RAGEngine:
    """A simple RAG engine."""

    def __init__(self):
        print("RAG Engine initialized.")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50,
        )

        print("Loading embedding model...")

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.index = None
        self.chunks = []

    def load_pdf(self, pdf_path: str) -> str:
        """Read a PDF and return its text."""

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def split_text(self, text: str):
        """Split text into chunks."""

        return self.text_splitter.split_text(text)

    def create_embeddings(self, chunks):
        """Convert text chunks into embeddings."""

        embeddings = self.embedding_model.encode(
            chunks,
            convert_to_numpy=True,
        )

        return embeddings

    def build_index(self, embeddings):
        """Build a FAISS vector index."""

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.asarray(embeddings, dtype=np.float32)
        )

        print(
            f"FAISS index created with {self.index.ntotal} vectors."
        )

    def answer_question(self, question: str) -> str:
        """Temporary answer method for testing embeddings and FAISS."""

        pdf_file = Path("documents") / "sample.pdf"

        document = self.load_pdf(str(pdf_file))

        chunks = self.split_text(document)

        embeddings = self.create_embeddings(chunks)

        self.build_index(embeddings)

        return (
            f"Question: {question}\n\n"
            f"Number of chunks: {len(chunks)}\n"
            f"Embedding shape: {embeddings.shape}\n"
            f"Vectors stored: {self.index.ntotal}\n\n"
            f"First Chunk:\n\n"
            f"{chunks[0]}"
        )