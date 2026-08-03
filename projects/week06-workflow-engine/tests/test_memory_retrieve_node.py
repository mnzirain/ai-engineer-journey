import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState
from nodes.memory_retrieve_node import MemoryRetrieveNode

state = WorkflowState("")

state.memory["name"] = "Mike"

node = MemoryRetrieveNode()

state = node.run(state)

print("Response:", state.response)