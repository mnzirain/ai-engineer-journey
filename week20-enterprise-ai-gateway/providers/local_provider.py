class LocalProvider:

    def generate(self, prompt):

        return {
            "provider": "Local",
            "response": f"Generated response for: {prompt}"
        }