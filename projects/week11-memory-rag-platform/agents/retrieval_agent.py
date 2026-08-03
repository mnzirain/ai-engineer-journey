from langchain_core.messages import AIMessage

from services.retrieval_service import RetrievalService


class RetrievalAgent:
    """
    Enterprise Retrieval Agent
    """

    @staticmethod
    def execute(state):

        print("Retrieval Agent Executed")

        user_message = state["messages"][-1].content.lower()

        if "my name" in user_message:

            result = RetrievalService.retrieve("user_name")

            if result:

                return {
                    "messages": [
                        AIMessage(
                            content=f"Your name is {result['user_name']}."
                        )
                    ]
                }

        return {
            "messages": [
                AIMessage(
                    content="No relevant memory found."
                )
            ]
        }