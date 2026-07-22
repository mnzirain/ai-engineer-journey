import re

from nodes.base_node import BaseNode
from state import WorkflowState


class MemoryNode(BaseNode):

    def __init__(self):

        super().__init__("Memory")

    def run(self, state: WorkflowState) -> WorkflowState:

        message = state.user_input

        if "my name is" in message.lower():

            match = re.search(r"my name is\s+(.+)", message, re.IGNORECASE)

            if match:

                name = match.group(1).strip()

                state.memory["name"] = name

                state.response = f"Nice to meet you, {name}."

        elif "what is my name" in message.lower():

            name = state.memory.get("name")

            if name:

                state.response = f"Your name is {name}."

            else:

                state.response = "I don't know your name yet."

        return state