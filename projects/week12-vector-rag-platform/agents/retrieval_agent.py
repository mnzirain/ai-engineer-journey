from langchain_core.messages import AIMessage

from services.retrieval_service import RetrievalService


class RetrievalAgent:
    """
    Enterprise Retrieval Agent
    """

    @staticmethod
    def execute(state):

        print("Retrieval Agent Executed")

        query = state["messages"][-1].content

        results = RetrievalService.search(query)

        context = "\n\n".join(results)

        return {
            "messages": [
                AIMessage(
                    content=f"Retrieved Context:\n\n{context}"
                )
            ]
        }