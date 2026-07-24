from langgraph.graph import StateGraph, START, END
from models.workflow_state import WorkflowState
from langchain_core.messages import AIMessage


def memory_node(state):
    print("Memory Node Executed")

    return {
        "messages": [
            AIMessage(
                content="Memory workflow placeholder."
            )
        ]
    }


builder = StateGraph(WorkflowState)

builder.add_node("memory", memory_node)

builder.add_edge(START, "memory")

builder.add_edge("memory", END)

memory_graph = builder.compile()