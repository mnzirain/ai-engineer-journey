from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class RAGEngine:
    """A simple RAG engine."""

    def __init__(self):
        print("RAG Engine initialized.")

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        )

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

        chunks = self.text_splitter.split_text(text)

        return chunks

    def answer_question(self, question: str) -> str:

        pdf_file = Path("documents") / "sample.pdf"

        document = self.load_pdf(str(pdf_file))

        chunks = self.split_text(document)

        answer = (
            f"Question: {question}\n\n"
            f"Number of chunks: {len(chunks)}\n\n"
            f"First Chunk:\n\n"
            f"{chunks[0]}"
        )

        return answer