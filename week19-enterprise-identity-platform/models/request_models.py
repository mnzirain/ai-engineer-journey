from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenRequest(BaseModel):
    refresh_token: str