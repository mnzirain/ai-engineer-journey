from pathlib import Path

from pypdf import PdfReader


class RAGEngine:
    """A simple RAG engine for loading and reading PDF documents."""

    def __init__(self):
        print("RAG Engine initialized.")

    def load_pdf(self, pdf_path: str) -> str:
        """Load a PDF and return all extracted text."""

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    def answer_question(self, question: str) -> str:
        """Placeholder response until retrieval is implemented."""

        pdf_file = Path("documents") / "sample.pdf"

        document_text = self.load_pdf(str(pdf_file))

        return (
            f"Question: {question}\n\n"
            f"Document Preview:\n"
            f"{document_text[:800]}"
        )