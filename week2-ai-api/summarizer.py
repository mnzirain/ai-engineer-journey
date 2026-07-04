from transformers import pipeline

print("Loading AI model... (This may take a minute the first time.)")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text: str) -> str:
    print("\n========== INPUT ==========")
    print(text)

    result = summarizer(
        text,
        max_length=40,
        min_length=10,
        do_sample=False,
        truncation=True
    )

    print("\n========== OUTPUT ==========")
    print(result)

    return result[0]["summary_text"]