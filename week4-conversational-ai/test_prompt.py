from memory import ConversationMemory
from prompt_template import build_prompt

memory = ConversationMemory()

memory.add_user_message("Hello")

memory.add_ai_message("Hi Mike!")

memory.add_user_message("My name is Mike.")

memory.add_ai_message("Nice to meet you Mike!")

prompt = build_prompt(
    memory.get_history(),
    "What is my name?"
)

print(prompt)