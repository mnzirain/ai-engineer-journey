from pydantic import BaseModel
from typing import Dict, Any, Optional


class MCPRequest(BaseModel):
    """
    Enterprise MCP Request
    """

    session_id: str

    tool: str

    input: Dict[str, Any]

    metadata: Optional[Dict[str, Any]] = {}