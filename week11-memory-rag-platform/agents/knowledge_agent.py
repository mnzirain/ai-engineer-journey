from langchain_core.messages import AIMessage


class KnowledgeAgent:

    @staticmethod
    def execute(state):

        print("Knowledge Agent Executed")

        return {
            "messages": [
                AIMessage(
                    content="Knowledge agent completed successfully."
                )
            ]
        }