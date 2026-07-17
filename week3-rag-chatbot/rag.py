from pathlib import Path

import faiss
import numpy as np
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

from llm import LLM
from prompt_template import build_prompt


class RAGEngine:
    """
    Production-ready Retrieval Augmented Generation Engine.

    Responsibilities
    ----------------
    - Load every PDF in /documents
    - Split into chunks
    - Generate embeddings
    - Build a FAISS vector index
    - Retrieve relevant chunks
    - Send context to the LLM
    """

    def __init__(self):

        print("RAG Engine initialized.")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=40,
        )

        print("Loading embedding model...")

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.llm = LLM()

        self.index = None

        # Each item will look like:
        #
        # {
        #     "text": "...",
        #     "source": "sample.pdf"
        # }
        #
        self.chunks = []

        self.initialize()

    def initialize(self):
        """
        Build the vector database once during startup.
        """

        documents_folder = Path("documents")

        pdf_files = sorted(
            documents_folder.glob("*.pdf")
        )

        self.chunks = []

        if not pdf_files:
            print("No PDF documents found.")
            return

        print()

        print("Loading documents...")

        for pdf_file in pdf_files:

            print(f"Loading {pdf_file.name}")

            document = self.load_pdf(
                str(pdf_file)
            )

            chunks = self.split_text(document)

            for chunk in chunks:

                self.chunks.append(
                    {
                        "text": chunk,
                        "source": pdf_file.name,
                    }
                )

        print()

        print(
            f"Loaded {len(self.chunks)} chunks "
            f"from {len(pdf_files)} PDF(s)."
        )

        print("Generating embeddings...")

        embeddings = self.create_embeddings(
            [
                chunk["text"]
                for chunk in self.chunks
            ]
        )

        print("Building FAISS index...")

        self.build_index(
            embeddings
        )

        print("RAG Engine ready!")

        print()

    def load_pdf(self, pdf_path: str) -> str:
        """
        Read an entire PDF into one string.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text

    def split_text(self, text: str):
        """
        Split document into overlapping chunks.
        """

        return self.text_splitter.split_text(text)

    def create_embeddings(self, chunks):
        """
        Convert chunks into embeddings.
        """

        embeddings = self.embedding_model.encode(
            chunks,
            convert_to_numpy=True,
        )

        return embeddings

    def build_index(self, embeddings):
        """
        Build FAISS vector index.
        """

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            np.asarray(
                embeddings,
                dtype=np.float32,
            )
        )

    def search(self, question: str, k: int = 3):
        """
        Search the FAISS index and return the
        top-k matching chunks with metadata.
        """

        question_embedding = self.embedding_model.encode(
            [question],
            convert_to_numpy=True,
        )

        distances, indices = self.index.search(
            np.asarray(question_embedding, dtype=np.float32),
            k,
        )

        results = []

        for rank, chunk_index in enumerate(indices[0]):

            if chunk_index == -1:
                continue

            results.append(
                {
                    "text": self.chunks[chunk_index]["text"],
                    "source": self.chunks[chunk_index]["source"],
                    "distance": float(distances[0][rank]),
                }
            )

        return results

    def answer_question(self, question: str) -> str:
        """
        Retrieve relevant context and ask the LLM.
        """

        retrieved_chunks = self.search(question)

        print("\n================ RETRIEVAL DEBUGGER ================\n")

        for rank, chunk in enumerate(retrieved_chunks, start=1):

            print(f"Rank {rank}")
            print(f"Source   : {chunk['source']}")
            print(f"Distance : {chunk['distance']:.4f}")
            print("-" * 60)
            print(chunk["text"][:300])
            print("\n")

        print("====================================================\n")

        context = "\n\n".join(
            chunk["text"] for chunk in retrieved_chunks
        )

        prompt = build_prompt(
            question=question,
            context=context,
        )

        answer = self.llm.generate(prompt)

        return answer