from langchain_core.messages import AIMessage
from services.memory_service import MemoryService


class MemoryAgent:
    """
    Memory Specialist Agent
    """

    @staticmethod
    def execute(state):

        print("Memory Agent Executed")

        MemoryService.save("user", "Mike")

        return {
            "messages": [
                AIMessage(
                    content=f"Memory updated: {MemoryService.show()}"
                )
            ]
        }