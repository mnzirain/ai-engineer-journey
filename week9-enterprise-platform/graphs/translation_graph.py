from langgraph.graph import StateGraph, START, END

from models.workflow_state import WorkflowState

from langchain_core.messages import AIMessage


def translation_node(state):

    print("Translation Node Executed")

    return {
        "messages": [
            AIMessage(
                content="Translation workflow is ready."
            )
        ]
    }


builder = StateGraph(WorkflowState)

builder.add_node("translation", translation_node)

builder.add_edge(START, "translation")

builder.add_edge("translation", END)

translation_graph = builder.compile()