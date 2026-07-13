from fastapi import FastAPI

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


@app.get("/ask")
def ask(question: str):
    answer = rag_engine.answer_question(question)

    return {
        "question": question,
        "answer": answer,
    }