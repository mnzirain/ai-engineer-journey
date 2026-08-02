from gateway.request_router import RequestRouter
from middleware.monitoring import Monitoring
from middleware.logging import LoggingMiddleware


class GatewayEngine:

    def __init__(self):
        self.router = RequestRouter()

    def providers(self):
        return {
            "providers": [
                "OpenAI",
                "Hugging Face",
                "Local"
            ]
        }

    def models(self):
        return {
            "models": [
                "GPT-4",
                "Llama",
                "Mistral"
            ]
        }

    def generate(self, request):

        Monitoring.request()

        LoggingMiddleware.log(
            "/generate",
            request.provider
        )

        return self.router.route(request)

    def metrics(self):

        return Monitoring.get()