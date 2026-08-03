from fastapi import FastAPI
from pydantic import BaseModel

from chat import ChatEngine


app = FastAPI(
    title="Conversational AI API",
    description="A production-ready conversational AI with memory.",
    version="1.0.0",
)

chat_engine = ChatEngine()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Conversational AI API is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer = chat_engine.chat(request.message)

    return {
        "user": request.message,
        "assistant": answer,
    }


@app.post("/clear-memory")
def clear_memory():

    chat_engine.clear_memory()

    return {
        "message": "Conversation memory cleared."
    }


@app.get("/history")
def history():

    return chat_engine.memory.get_history()