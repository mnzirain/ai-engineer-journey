import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.memory_node import MemoryNode

memory = MemoryNode()

# Store name

state = WorkflowState("My name is Mike")

state = memory.run(state)

print()

print(state.response)

# Ask again using the SAME state

state.user_input = "What is my name?"

state = memory.run(state)

print(state.response)