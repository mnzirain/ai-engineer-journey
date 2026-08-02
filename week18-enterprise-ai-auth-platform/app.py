from fastapi import FastAPI

from models.request_models import MCPRequest
from core.mcp_server import MCPServer

app = FastAPI(
    title="Week 18 Enterprise AI Authentication Platform"
)

server = MCPServer()


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Authentication Platform",
        "week": 18
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/mcp")
def process_request(request: MCPRequest):
    return server.process(request)