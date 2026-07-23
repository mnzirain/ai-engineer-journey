from langgraph.graph import StateGraph, START, END

from state.workflow_state import WorkflowState

from nodes.planner_node import planner_node
from nodes.greeting_node import greeting_node
from nodes.knowledge_node import knowledge_node


workflow = StateGraph(WorkflowState)

workflow.add_node("planner", planner_node)
workflow.add_node("greeting", greeting_node)
workflow.add_node("knowledge", knowledge_node)


workflow.add_edge(START, "planner")


def route_workflow(state):

    return state["route"]


workflow.add_conditional_edges(

    "planner",

    route_workflow,

    {

        "greeting": "greeting",

        "knowledge": "knowledge",

    },

)

workflow.add_edge("greeting", END)

workflow.add_edge("knowledge", END)

graph = workflow.compile()