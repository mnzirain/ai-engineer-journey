from langchain_core.messages import HumanMessage

from planner.enterprise_planner import EnterprisePlanner
from agents.supervisor_agent import SupervisorAgent
from graphs.supervisor_graph import supervisor_graph


def run(user_input: str):

    planner = EnterprisePlanner()

    route = planner.select_workflow(user_input)

    SupervisorAgent.delegate(user_input)

    state = {
        "messages": [HumanMessage(content=user_input)],
        "route": route,
    }

    result = supervisor_graph.invoke(state)

    return result


tests = [
    "hello Mike",
    "15 + 25",
    "what is artificial intelligence?",
    "translate hello to french",
    "remember that my name is Mike",
]


for i, test in enumerate(tests, start=1):

    print(f"\n========== TEST {i} ==========\n")

    response = run(test)

    for message in response["messages"]:
        print(type(message).__name__, ":", message.content)