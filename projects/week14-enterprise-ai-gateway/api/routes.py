from fastapi import APIRouter
from pydantic import BaseModel

from registry.service_registry import ServiceRegistry

router = APIRouter()


class SearchRequest(BaseModel):
    query: str


@router.get("/")
def home():

    return {
        "service": "Enterprise AI Gateway",
        "status": "running",
        "version": "1.0.0"
    }


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.get("/stats")
def stats():

    return ServiceRegistry.knowledge.stats()


@router.post("/search")
def search(request: SearchRequest):

    results = ServiceRegistry.knowledge.search(request.query)

    return {
        "query": request.query,
        "results": results
    }