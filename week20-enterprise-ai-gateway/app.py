from fastapi import FastAPI, Depends
from fastapi.security import APIKeyHeader

from gateway.gateway_engine import GatewayEngine
from middleware.authentication import AuthenticationMiddleware
from middleware.rate_limiter import RateLimiter
from models.gateway_models import GenerateRequest

app = FastAPI(
    title="Week 20 Enterprise AI Gateway",
    version="1.0.0",
    description="""
Enterprise AI Gateway

• Authentication

• Authorization

• Multi-Provider Routing

• Enterprise Middleware

• Monitoring

• Logging
"""
)

gateway = GatewayEngine()

api_key_header = APIKeyHeader(
    name="api-key",
    auto_error=True
)


@app.get("/")
def root():

    return {
        "status": "running",
        "service": "Enterprise AI Gateway",
        "week": 20,
        "version": "1.0.0"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "Enterprise AI Gateway"
    }


@app.get("/providers")
def providers():

    return gateway.providers()


@app.get("/models")
def models():

    return gateway.models()


@app.post("/generate")
def generate(
    request: GenerateRequest,
    api_key: str = Depends(api_key_header)
):

    AuthenticationMiddleware.authenticate(api_key)

    if not RateLimiter.check(api_key):

        return {
            "status": "failed",
            "reason": "Rate limit exceeded"
        }

    return gateway.generate(request)


@app.get("/metrics")
def metrics():

    return gateway.metrics()