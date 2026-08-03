import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.memory_store_node import MemoryStoreNode

state = WorkflowState("My name is Mike")

node = MemoryStoreNode()

state = node.run(state)

print("Memory:", state.memory)
print("Response:", state.response)