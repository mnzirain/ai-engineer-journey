from fastapi import FastAPI
from pydantic import BaseModel

from engine import OrchestratorEngine

app = FastAPI(
    title="Week 7 Multi-Agent Orchestrator",
    version="1.0.0"
)

engine = OrchestratorEngine()


class UserRequest(BaseModel):
    message: str


@app.get("/")
def home():

    return {
        "message": "Week 7 Multi-Agent Orchestrator is running."
    }


@app.post("/workflow")
def workflow(request: UserRequest):

    state = engine.run(request.message)

    return {
        "response": state.response
    }