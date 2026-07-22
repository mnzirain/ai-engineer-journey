import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from planner import Planner
from state import WorkflowState


planner = Planner()

examples = [
    "Hello",
    "20 + 30",
    "My name is Mike",
    "What is my name?",
    "Tell me about AI"
]

for message in examples:

    state = WorkflowState(user_input=message)

    planner.create_plan(state)

    print("=" * 40)
    print("User:", message)
    print("Plan:", state.plan)