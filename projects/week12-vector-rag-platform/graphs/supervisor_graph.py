from langgraph.graph import StateGraph, END

from models.workflow_state import WorkflowState

from agents.retrieval_agent import RetrievalAgent


def supervisor(state: WorkflowState):

    print(f"\nSupervisor routing -> {state['route']}")

    if state["route"] == "retrieval":

        return RetrievalAgent.execute(state)

    return {
        "messages": state["messages"]
    }


builder = StateGraph(WorkflowState)

builder.add_node("supervisor", supervisor)

builder.set_entry_point("supervisor")

builder.add_edge("supervisor", END)

supervisor_graph = builder.compile()