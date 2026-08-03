from transformers import pipeline


class LLM:
    """
    Wrapper around the Hugging Face FLAN-T5 model.
    """

    def __init__(self):

        print("Loading language model...")

        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
        )

        print("Language model ready!")

    def generate(self, prompt: str) -> str:

        result = self.generator(
            prompt,
            max_new_tokens=80,
            do_sample=False,
        )

        return result[0]["generated_text"]