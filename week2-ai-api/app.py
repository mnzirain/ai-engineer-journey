from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import summarize_text

app = FastAPI(
    title="Mike's AI Summarizer API",
    description="An AI-powered text summarization API using Hugging Face Transformers.",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Welcome to Mike's AI Summarizer API!"
    }

@app.post("/summarize")
def summarize(request: TextRequest):
    summary = summarize_text(request.text)

    return {
        "summary": summary
    }