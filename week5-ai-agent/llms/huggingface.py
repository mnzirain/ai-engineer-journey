from transformers import pipeline

from .base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    """
    Hugging Face implementation of the language model interface.
    """

    def __init__(self):

        print("Loading Hugging Face model...")

        self.generator = pipeline(
            task="text2text-generation",
            model="google/flan-t5-base",
        )

        print("Hugging Face model ready!")

    def generate(self, prompt: str) -> str:

        result = self.generator(
            prompt,
            max_new_tokens=80,
            do_sample=False,
        )

        return result[0]["generated_text"].strip()