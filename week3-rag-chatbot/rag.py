from pathlib import Path

import faiss
import numpy as np
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from llm import LLM
from prompt_template import build_prompt


class RAGEngine:
    """A simple RAG engine."""

    def __init__(self):
        print("RAG Engine initialized.")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=150,
            chunk_overlap=30,
        )

        print("Loading embedding model...")

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.llm = LLM()

        self.index = None
        self.chunks = []

        self.initialize()

    def initialize(self):
        """
        Load the document and build the FAISS index once.
        """

        print("Loading PDF document...")

        pdf_file = Path("documents") / "sample.pdf"

        document = self.load_pdf(str(pdf_file))

        print("Splitting document...")

        self.chunks = self.split_text(document)

        print(f"Created {len(self.chunks)} chunks.")

        print("Generating embeddings...")

        embeddings = self.create_embeddings(self.chunks)

        print("Building FAISS index...")

        self.build_index(embeddings)

        print("RAG Engine ready!")

    def load_pdf(self, pdf_path: str) -> str:

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def split_text(self, text: str):

        return self.text_splitter.split_text(text)

    def create_embeddings(self, chunks):

        embeddings = self.embedding_model.encode(
            chunks,
            convert_to_numpy=True,
        )

        return embeddings

    def build_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.asarray(embeddings, dtype=np.float32)
        )

    def search(self, question, k=3):

        question_embedding = self.embedding_model.encode(
            [question],
            convert_to_numpy=True,
        )

        distances, indices = self.index.search(
            np.asarray(question_embedding, dtype=np.float32),
            k,
        )

        results = []

        for rank in range(k):

            chunk_index = indices[0][rank]

            results.append(
                self.chunks[chunk_index]
            )

        return results

    def answer_question(self, question: str):

        retrieved_chunks = self.search(question)

        context = "\n\n".join(retrieved_chunks)

        prompt = build_prompt(
            question,
            context,
        )

        answer = self.llm.generate(prompt)

        return answer