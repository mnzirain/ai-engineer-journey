from chat import ChatEngine

chatbot = ChatEngine()

print("\nAI Assistant Ready!")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = chatbot.chat(question)

    print(f"\nAI: {answer}\n")