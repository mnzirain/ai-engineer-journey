from fastapi import FastAPI
from pydantic import BaseModel

from agent import AIAgent

app = FastAPI(
    title="Week 5 - Modular AI Agent",
    description="A modular AI Agent with Planning, Routing, Memory, Tool Registry and LLM.",
    version="1.0.0",
)

agent = AIAgent()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    user: str
    assistant: str


@app.get("/")
def home():
    return {
        "message": "Week 5 Modular AI Agent API is running!"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = agent.chat(request.message)

    return ChatResponse(
        user=request.message,
        assistant=answer,
    )