from pydantic import BaseModel
from typing import Dict, Any, Optional


class MCPResponse(BaseModel):
    """
    Enterprise MCP Response
    """

    session_id: str

    tool: str

    status: str

    output: Dict[str, Any]

    metadata: Optional[Dict[str, Any]] = {}