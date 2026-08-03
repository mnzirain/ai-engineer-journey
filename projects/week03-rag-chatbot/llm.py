"""
Language Model wrapper.
"""

from transformers import pipeline


class LLM:
    """
    Wrapper around the Hugging Face language model.
    """

    def __init__(self):
        print("Loading language model...")

        self.generator = pipeline(
            task="text2text-generation",
            model="google/flan-t5-base",
        )

    def generate(self, prompt: str) -> str:
        """
        Generate an answer from the language model.
        """

        response = self.generator(
            prompt,
            max_new_tokens=80,
            min_new_tokens=15,
            do_sample=False,
        )

        return response[0]["generated_text"].strip()