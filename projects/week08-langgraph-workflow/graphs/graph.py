from langgraph.graph import StateGraph, START, END

from state.workflow_state import WorkflowState

from nodes.planner_node import planner_node
from nodes.greeting_node import greeting_node
from nodes.knowledge_node import knowledge_node
from nodes.calculator_node import calculator_node


# Create workflow
workflow = StateGraph(WorkflowState)

# Register nodes
workflow.add_node("planner", planner_node)
workflow.add_node("greeting", greeting_node)
workflow.add_node("calculator", calculator_node)
workflow.add_node("knowledge", knowledge_node)


# Routing function
def route_workflow(state):
    return state["route"]


# Workflow
workflow.add_edge(START, "planner")

workflow.add_conditional_edges(
    "planner",
    route_workflow,
    {
        "greeting": "greeting",
        "calculator": "calculator",
        "memory": "knowledge",      # temporary placeholder
        "knowledge": "knowledge",
    },
)

workflow.add_edge("greeting", END)
workflow.add_edge("calculator", END)
workflow.add_edge("knowledge", END)


# Compile graph
graph = workflow.compile()