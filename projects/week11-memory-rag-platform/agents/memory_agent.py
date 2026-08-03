from langchain_core.messages import AIMessage

from services.memory_service import MemoryService


class MemoryAgent:
    """
    Enterprise Memory Agent
    """

    @staticmethod
    def execute(state):

        print("Memory Agent Executed")

        user_message = state["messages"][-1].content

        if "name is" in user_message.lower():

            name = user_message.split("is")[-1].strip()

            MemoryService.remember("user_name", name)

            return {
                "messages": [
                    AIMessage(
                        content=f"I'll remember that your name is {name}."
                    )
                ]
            }

        return {
            "messages": [
                AIMessage(
                    content="Nothing new to remember."
                )
            ]
        }