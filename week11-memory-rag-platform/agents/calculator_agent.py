from langchain_core.messages import AIMessage


class CalculatorAgent:

    @staticmethod
    def execute(state):

        print("Calculator Agent Executed")

        return {
            "messages": [
                AIMessage(
                    content="The answer is 40."
                )
            ]
        }