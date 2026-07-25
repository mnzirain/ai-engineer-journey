from langchain_core.messages import AIMessage


class GreetingAgent:
    """
    Greeting Specialist Agent
    """

    @staticmethod
    def execute(state):

        print("Greeting Agent Executed")

        return {
            "messages": [
                AIMessage(
                    content="Hello! Welcome to the Enterprise Multi-Agent AI Platform."
                )
            ]
        }