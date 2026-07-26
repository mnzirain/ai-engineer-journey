from langchain_core.messages import HumanMessage

from planner.enterprise_planner import EnterprisePlanner
from graphs.supervisor_graph import supervisor_graph


def run(user_input: str):

    planner = EnterprisePlanner()

    route = planner.select_workflow(user_input)

    state = {
        "messages": [
            HumanMessage(content=user_input)
        ],
        "route": route,
    }

    result = supervisor_graph.invoke(state)

    return result


tests = [

    "hello",

    "15 + 25",

    "what is artificial intelligence?",

    "translate hello to french",

    "remember that my name is Mike",

    "what is my name",

]


for i, test in enumerate(tests, start=1):

    print("\n" + "=" * 50)
    print(f"TEST {i}")
    print("=" * 50)

    response = run(test)

    for message in response["messages"]:

        print(type(message).__name__, ":", message.content)