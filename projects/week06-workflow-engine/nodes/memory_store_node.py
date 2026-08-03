from nodes.base_node import BaseNode


class MemoryStoreNode(BaseNode):

    name = "MemoryStore"

    def run(self, state):

        words = state.user_input.split()

        if "name" in words:

            index = words.index("name")

            if index + 2 < len(words):

                state.memory["name"] = words[index + 2]

                state.response = f"Nice to meet you, {words[index + 2]}."

            else:

                state.response = "I didn't catch your name."

        return state