from pydantic import BaseModel


class APIKeyRequest(BaseModel):
    api_key: str


class User(BaseModel):
    username: str
    role: str


class AuthResult(BaseModel):
    authenticated: bool
    username: str
    role: str