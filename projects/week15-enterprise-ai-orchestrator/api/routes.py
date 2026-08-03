from fastapi import APIRouter
from pydantic import BaseModel

from core.workflow_engine import WorkflowEngine

router = APIRouter()

engine = WorkflowEngine()


class QueryRequest(BaseModel):
    query: str


@router.get("/")
def home():

    return {
        "message": "Enterprise AI Platform v2 Running"
    }


@router.post("/ask")
def ask(request: QueryRequest):

    return engine.process(request.query)