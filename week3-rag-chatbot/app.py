from pathlib import Path
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
)

from rag import RAGEngine


app = FastAPI(
    title="AI Document Chat API",
    description="A Retrieval-Augmented Generation (RAG) API for chatting with PDF documents.",
    version="1.0.0",
)

rag_engine = RAGEngine()


@app.get("/")
def root():
    return {
        "message": "Welcome to the AI Document Chat API!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF into the knowledge base.
    """

    documents_folder = Path("documents")
    documents_folder.mkdir(exist_ok=True)

    destination = documents_folder / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    rag_engine.initialize()

    return {
        "message": f"{file.filename} uploaded successfully.",
        "documents": len(list(documents_folder.glob("*.pdf")))
    }


@app.get("/ask")
def ask(question: str):

    result = rag_engine.answer_question(question)

    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
    }