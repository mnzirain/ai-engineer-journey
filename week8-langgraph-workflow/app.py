from langchain_core.messages import HumanMessage

from services.planner_service import EnterprisePlanner
from graphs.workflow_registry import WorkflowRegistry


planner = EnterprisePlanner()

registry = WorkflowRegistry()


tests = [

    "Hello Mike",

    "20 + 30",

    "What is Artificial Intelligence?"

]


for i, test in enumerate(tests, start=1):

    print(f"\n========== TEST {i} ==========\n")

    workflow_name = planner.classify(test)

    print("Selected Workflow:", workflow_name)

    graph = registry.get(workflow_name)

    result = graph.invoke(

        {

            "messages": [

                HumanMessage(content=test)

            ]

        }

    )

    for msg in result["messages"]:

        print(type(msg).__name__, ":", msg.content)