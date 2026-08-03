from langchain_core.messages import AIMessage


class GreetingAgent:

    @staticmethod
    def execute(state):

        print("Greeting Agent Executed")

        return {
            "messages": [
                AIMessage(
                    content="Hello! Welcome to the Enterprise Memory & RAG Platform."
                )
            ]
        }