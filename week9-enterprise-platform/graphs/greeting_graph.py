from langgraph.graph import StateGraph, START, END

from models.workflow_state import WorkflowState

from langchain_core.messages import AIMessage


def greeting_node(state):

    print("Greeting Node Executed")

    return {
        "messages": [
            AIMessage(
                content="Hello! Welcome to the Enterprise AI Platform."
            )
        ]
    }


builder = StateGraph(WorkflowState)

builder.add_node("greeting", greeting_node)

builder.add_edge(START, "greeting")

builder.add_edge("greeting", END)

greeting_graph = builder.compile()