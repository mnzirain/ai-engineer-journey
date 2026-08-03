from transformers import pipeline

print("Loading AI model... (This may take a minute the first time.)")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text: str) -> str:
    """
    Summarize input text using a pretrained Hugging Face model.
    """
    result = summarizer(
        text,
        max_length=80,
        min_length=25,
        do_sample=False
    )

    return result[0]["summary_text"]