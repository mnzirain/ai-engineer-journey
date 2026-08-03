from fastapi import FastAPI
from pydantic import BaseModel

from core.mcp_server import MCPServer

app = FastAPI(
    title="Week 17 - Enterprise MCP Server",
    description="Enterprise Model Context Protocol (MCP) Server",
    version="1.0"
)

mcp = MCPServer()


class ToolRequest(BaseModel):
    tool: str
    input: dict


@app.get("/")
def root():
    return {
        "message": "Week 17 - Enterprise Model Context Protocol Server",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Enterprise MCP Server"
    }


@app.get("/mcp/tools")
def list_tools():
    return mcp.list_tools()


@app.post("/mcp/invoke")
def invoke_tool(request: ToolRequest):
    response = mcp.invoke(
        request.tool,
        request.input
    )

    return response.model_dump()