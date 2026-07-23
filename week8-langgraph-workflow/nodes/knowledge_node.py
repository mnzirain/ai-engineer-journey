from langchain_core.messages import AIMessage


def knowledge_node(state):
    print("Knowledge Node Executed")

    return {
        "messages": [
            AIMessage(
                content="Knowledge workflow completed successfully."
            )
        ]
    }