from pydantic import BaseModel


class MCPRequest(BaseModel):
    api_key: str
    tool: str
    payload: dict