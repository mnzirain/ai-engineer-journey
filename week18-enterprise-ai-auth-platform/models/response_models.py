from pydantic import BaseModel
from typing import Any, Dict


class APIResponse(BaseModel):
    status: str
    message: str
    data: Dict[str, Any] | None = None