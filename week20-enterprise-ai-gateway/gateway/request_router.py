from providers.openai_provider import OpenAIProvider
from providers.huggingface_provider import HuggingFaceProvider
from providers.local_provider import LocalProvider


class RequestRouter:

    def __init__(self):
        self.openai = OpenAIProvider()
        self.hf = HuggingFaceProvider()
        self.local = LocalProvider()

    def route(self, request):

        if request.provider == "OpenAI":
            return self.openai.generate(request.prompt)

        if request.provider == "Hugging Face":
            return self.hf.generate(request.prompt)

        return self.local.generate(request.prompt)