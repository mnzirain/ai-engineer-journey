from langgraph.graph import StateGraph, START, END

from models.workflow_state import WorkflowState

from agents.greeting_agent import GreetingAgent
from agents.calculator_agent import CalculatorAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.translation_agent import TranslationAgent
from agents.memory_agent import MemoryAgent


def supervisor_router(state: WorkflowState):
    route = state["route"]

    print(f"\nSupervisor routing -> {route}")

    return route


builder = StateGraph(WorkflowState)

builder.add_node("greeting", GreetingAgent.execute)
builder.add_node("calculator", CalculatorAgent.execute)
builder.add_node("knowledge", KnowledgeAgent.execute)
builder.add_node("translation", TranslationAgent.execute)
builder.add_node("memory", MemoryAgent.execute)

builder.add_conditional_edges(
    START,
    supervisor_router,
    {
        "greeting": "greeting",
        "calculator": "calculator",
        "knowledge": "knowledge",
        "translation": "translation",
        "memory": "memory",
    },
)

builder.add_edge("greeting", END)
builder.add_edge("calculator", END)
builder.add_edge("knowledge", END)
builder.add_edge("translation", END)
builder.add_edge("memory", END)

supervisor_graph = builder.compile()