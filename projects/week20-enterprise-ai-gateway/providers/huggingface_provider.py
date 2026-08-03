class HuggingFaceProvider:

    def generate(self, prompt):

        return {
            "provider": "Hugging Face",
            "response": f"Generated response for: {prompt}"
        }