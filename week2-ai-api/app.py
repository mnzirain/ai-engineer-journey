import logging
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from summarizer import summarize_text

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Mike's AI Summarizer API",
    description="An AI-powered text summarization API using Hugging Face Transformers.",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=50,
        max_length=5000,
        description="Text to summarize"
    )

@app.get("/")
def home():
    return {
        "message": "Welcome to Mike's AI Summarizer API!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Summarizer API",
        "version": "1.0.0"
    }

@app.post("/summarize")
def summarize(request: TextRequest):
    start_time = time.time()

    logger.info("Received summarization request.")

    try:
        summary = summarize_text(request.text)

        elapsed = time.time() - start_time

        logger.info(
            f"Summarization completed successfully in {elapsed:.2f} seconds."
        )

        return {
            "summary": summary
        }

    except Exception as e:
        logger.error(f"Summarization failed: {e}")

        raise HTTPException(
            status_code=500,
            detail=f"Failed to summarize text: {str(e)}"
        )