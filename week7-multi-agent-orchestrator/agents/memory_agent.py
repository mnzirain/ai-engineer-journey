from agents.base_agent import BaseAgent
from tools.memory_tool import MemoryTool


class MemoryAgent(BaseAgent):
    """
    Stores and retrieves user information using MemoryTool.
    """

    memory_tool = MemoryTool()

    def __init__(self):
        super().__init__("Memory Agent")

    def run(self, state):

        message = state.user_input.strip()

        # Memory Store
        if message and message.lower() != "what is my name?":

            self.memory_tool.store("name", message)

            state.response = f"Nice to meet you, {message}."

            return state

        # Memory Retrieve
        name = self.memory_tool.retrieve("name")

        if name:

            state.response = f"Your name is {name}."

        else:

            state.response = "I don't know your name yet."

        return state