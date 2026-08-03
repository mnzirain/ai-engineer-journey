import re

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