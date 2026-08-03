from langchain_core.messages import AIMessage


class TranslationAgent:

    @staticmethod
    def execute(state):

        print("Translation Agent Executed")

        return {
            "messages": [
                AIMessage(
                    content="Translation agent completed successfully."
                )
            ]
        }