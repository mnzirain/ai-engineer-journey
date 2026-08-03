from nodes.base_node import BaseNode


class MemoryRetrieveNode(BaseNode):

    name = "MemoryRetrieve"

    def run(self, state):

        if "name" in state.memory:

            state.response = f"Your name is {state.memory['name']}."

        else:

            state.response = "I don't know your name yet."

        return state