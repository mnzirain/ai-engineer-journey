from fastapi import FastAPI
from pydantic import BaseModel

from engine import WorkflowEngine

app = FastAPI(
    title="Workflow Engine API",
    description="Week 6 AI Workflow Engine",
    version="1.0"
)

engine = WorkflowEngine()


class WorkflowRequest(BaseModel):
    message: str


class WorkflowResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "message": "Workflow Engine API is running."
    }


@app.post("/workflow", response_model=WorkflowResponse)
def workflow(request: WorkflowRequest):

    state = engine.run(request.message)

    return WorkflowResponse(
        response=state.response
    )