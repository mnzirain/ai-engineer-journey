"""
Language Model wrapper.
"""

from transformers import pipeline


class LLM:

    def __init__(self):

        print("Loading language model...")

        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
        )

    def generate(self, prompt: str) -> str:

        response = self.generator(
            prompt,
            max_new_tokens=200,
            do_sample=False,
        )

        return response[0]["generated_text"]