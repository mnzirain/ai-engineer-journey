import re

from langgraph.graph import StateGraph, START, END

from models.workflow_state import WorkflowState

from langchain_core.messages import AIMessage


def calculator_node(state):

    print("Calculator Node Executed")

    text = state["messages"][-1].content

    numbers = list(map(int, re.findall(r"\d+", text)))

    if "+" in text and len(numbers) >= 2:
        answer = numbers[0] + numbers[1]

    elif "-" in text and len(numbers) >= 2:
        answer = numbers[0] - numbers[1]

    elif "*" in text and len(numbers) >= 2:
        answer = numbers[0] * numbers[1]

    elif "/" in text and len(numbers) >= 2:
        answer = numbers[0] / numbers[1]

    else:
        answer = "Invalid calculation."

    return {
        "messages": [
            AIMessage(content=f"The answer is {answer}.")
        ]
    }


builder = StateGraph(WorkflowState)

builder.add_node("calculator", calculator_node)

builder.add_edge(START, "calculator")

builder.add_edge("calculator", END)

calculator_graph = builder.compile()