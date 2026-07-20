from memory import ConversationMemory

memory = ConversationMemory()

memory.add_user_message("Hello")

memory.add_ai_message("Hi Mike!")

memory.add_user_message("My name is Mike.")

memory.add_ai_message("Nice to meet you, Mike!")

print(memory.get_history())