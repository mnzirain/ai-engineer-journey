from summarizer import summarize_text

print("=" * 60)
print("🤖 AI TEXT SUMMARIZER")
print("=" * 60)

text = input("\nPaste a long paragraph below:\n\n").strip()

if not text:
    print("\nPlease enter some text.")
    exit()

print("\nGenerating summary...\n")

summary = summarize_text(text)

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(summary)