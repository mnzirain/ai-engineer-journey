import sys
from pathlib import Path

# Add the project root to Python's import path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from state import WorkflowState

state = WorkflowState("Hello AI")

print()
print(state)
print()

print("User Input :", state.user_input)
print("Plan       :", state.plan)
print("Current    :", state.current_node)
print("Tool       :", state.tool)
print("Memory     :", state.memory)
print("Response   :", state.response)