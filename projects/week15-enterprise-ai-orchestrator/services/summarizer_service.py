from transformers import pipeline


class SummarizerService:

    def __init__(self):

        self.pipeline = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    def summarize(self, text: str):

        result = self.pipeline(
            text,
            max_length=80,
            min_length=20,
            do_sample=False
        )

        return result[0]["summary_text"]