from pydantic import BaseModel


class GenerateRequest(BaseModel):
    provider: str
    model: str
    prompt: str