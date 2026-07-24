from langchain_core.messages import HumanMessage

from planner.enterprise_planner import enterprise_planner
from services.router_service import RouterService


def run(message: str):
    """
    Executes the Enterprise AI Platform.
    """

    state = {
        "messages": [
            HumanMessage(content=message)
        ]
    }

    # Enterprise Planner decides which workflow to use
    planner_result = enterprise_planner(state)

    route = planner_result["route"]

    print(f"\nSelected Workflow: {route}")

    # Execute the selected workflow
    result = RouterService.execute(route, state)

    return result


# =====================================================
# TEST 1 - Greeting
# =====================================================

print("\n========== TEST 1 ==========\n")

response = run("Hello Mike")

for message in response["messages"]:
    print(type(message).__name__, ":", message.content)


# =====================================================
# TEST 2 - Calculator
# =====================================================

print("\n========== TEST 2 ==========\n")

response = run("15 + 25")

for message in response["messages"]:
    print(type(message).__name__, ":", message.content)


# =====================================================
# TEST 3 - Knowledge
# =====================================================

print("\n========== TEST 3 ==========\n")

response = run("What is Artificial Intelligence?")

for message in response["messages"]:
    print(type(message).__name__, ":", message.content)


# =====================================================
# TEST 4 - Translation
# =====================================================

print("\n========== TEST 4 ==========\n")

response = run("Translate Hello to French")

for message in response["messages"]:
    print(type(message).__name__, ":", message.content)


# =====================================================
# TEST 5 - Memory
# =====================================================

print("\n========== TEST 5 ==========\n")

response = run("Remember that my name is Mike")

for message in response["messages"]:
    print(type(message).__name__, ":", message.content)