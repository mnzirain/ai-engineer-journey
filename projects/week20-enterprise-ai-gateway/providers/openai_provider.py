class OpenAIProvider:

    def generate(self, prompt):

        return {
            "provider": "OpenAI",
            "response": f"Generated response for: {prompt}"
        }