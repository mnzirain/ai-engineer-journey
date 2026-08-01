from fastapi import FastAPI
from pydantic import BaseModel

from core.tool_router import ToolRouter
from core.tool_executor import ToolExecutor
from core.response_builder import ResponseBuilder

app = FastAPI(
    title="Week 16 – Enterprise Tool Calling Platform",
    description="Enterprise AI Tool Registry, Routing and Execution Platform",
    version="1.0.0",
)

# ---------------------------------------------------
# Request Model
# ---------------------------------------------------

class QueryRequest(BaseModel):
    query: str


# ---------------------------------------------------
# Enterprise Components
# ---------------------------------------------------

tool_router = ToolRouter()
tool_executor = ToolExecutor()
response_builder = ResponseBuilder()


# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Week 16 Enterprise Tool Calling Platform Running",
        "version": "1.0.0",
        "status": "healthy",
    }


# ---------------------------------------------------
# List Available Tools
# ---------------------------------------------------

@app.get("/tools")
def list_tools():
    return {
        "available_tools": tool_router.registry.describe_tools()
    }


# ---------------------------------------------------
# Execute Tool
# ---------------------------------------------------

@app.post("/tool")
def execute_tool(request: QueryRequest):

    tool = tool_router.route(request.query)

    if tool is None:
        return {
            "status": "error",
            "message": "No matching tool found."
        }

    result = tool_executor.execute(tool, request.query)

    return response_builder.build(tool.name, result)


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "platform": "Enterprise Tool Calling Platform",
        "version": "1.0.0"
    }