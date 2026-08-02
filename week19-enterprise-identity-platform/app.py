from fastapi import FastAPI

from models.request_models import LoginRequest
from core.identity_server import IdentityServer

from middleware.authentication import AuthenticationMiddleware
from middleware.authorization import AuthorizationMiddleware

app = FastAPI(
    title="Week 19 – Enterprise Identity & Access Management Platform",
    version="1.0.0",
    description="Enterprise OAuth2, JWT and Identity Management Platform"
)

identity = IdentityServer()

authentication = AuthenticationMiddleware()
authorization = AuthorizationMiddleware()


@app.get("/")
def root():

    return {
        "status": "running",
        "service": "Enterprise Identity Platform",
        "week": 19
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Enterprise Identity Platform",
        "authentication": "OAuth2 + JWT"
    }


@app.post("/login")
def login(request: LoginRequest):

    return identity.login(request)


@app.post("/refresh")
def refresh():

    return {
        "status": "success",
        "message": "Refresh token accepted.",
        "new_access_token": identity.jwt.create_access_token(
            "doctor"
        )
    }


@app.post("/logout")
def logout():

    return {
        "status": "success",
        "message": "Enterprise session terminated."
    }


@app.get("/protected")
def protected():

    token = {
        "token": "demo-token"
    }

    authenticated = authentication.authenticate(token)

    if not authenticated["authenticated"]:
        return authenticated

    allowed = authorization.authorize(
        "doctor",
        "search"
    )

    if not allowed:
        return {
            "status": "denied",
            "message": "Access denied."
        }

    return {
        "status": "success",
        "message": "Protected enterprise endpoint accessed successfully."
    }