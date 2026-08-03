import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.calculator_node import CalculatorNode

calculator = CalculatorNode()

tests = [
    "20 + 30",
    "calculate 12 * 8",
    "100 / 5",
]

for text in tests:

    state = WorkflowState(text)

    state = calculator.run(state)

    print()

    print("Input    :", text)
    print("Response :", state.response)