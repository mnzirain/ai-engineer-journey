import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.planner_node import PlannerNode

planner = PlannerNode()

tests = [
    "Hello",
    "My name is Mike",
    "What is my name?",
    "20 + 30",
    "Who invented Python?"
]

for text in tests:

    state = WorkflowState(text)

    state = planner.run(state)

    print()

    print("Input :", text)

    print("Plan  :", state.plan)