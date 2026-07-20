from llm import LLM
from memory import ConversationMemory
from prompt_template import build_prompt


class ChatEngine:
    """
    Production-ready conversational AI engine.
    """

    def __init__(self):
        self.memory = ConversationMemory()
        self.llm = LLM()

        print("Chat Engine initialized.")

    def chat(self, user_message: str):
        # Save the user's message
        self.memory.add_user_message(user_message)

        # Build a prompt using conversation history
        prompt = build_prompt(
            self.memory.get_history(),
            user_message,
        )

        print("\n========== PROMPT SENT TO MODEL ==========\n")
        print(prompt)
        print("\n==========================================\n")

        # Generate the AI response
        answer = self.llm.generate(prompt)

        # Save the AI response
        self.memory.add_ai_message(answer)

        return answer

    def clear_memory(self):
        self.memory.clear()