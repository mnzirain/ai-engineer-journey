import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.greeting_node import GreetingNode

state = WorkflowState("Hello")

node = GreetingNode()

state = node.run(state)

print()

print(state)

print()

print("Node:", node.name)
print("Response:", state.response)