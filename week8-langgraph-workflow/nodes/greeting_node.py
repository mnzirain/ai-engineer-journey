from langchain_core.messages import AIMessage


def greeting_node(state):
    print("Greeting Node Executed")

    return {
        "messages": [
            AIMessage(
                content="Hello Mike! Welcome to Enterprise LangGraph."
            )
        ]
    }