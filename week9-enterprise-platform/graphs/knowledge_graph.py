from langgraph.graph import StateGraph, START, END

from models.workflow_state import WorkflowState

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


builder = StateGraph(WorkflowState)

builder.add_node("knowledge", knowledge_node)

builder.add_edge(START, "knowledge")

builder.add_edge("knowledge", END)

knowledge_graph = builder.compile()