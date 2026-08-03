import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from condition import Condition

condition = Condition()

tests = [
    ["greeting"],
    ["calculator"],
    ["memory"],
    [],
]

for plan in tests:

    state = WorkflowState("")

    state.plan = plan

    print()

    print("Plan:", plan)

    print("Decision:", condition.evaluate(state))