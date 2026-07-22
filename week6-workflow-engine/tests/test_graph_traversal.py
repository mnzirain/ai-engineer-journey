import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph import WorkflowGraph

graph = WorkflowGraph()

graph.add_edge("Planner", "Greeting")
graph.add_edge("Greeting", "Memory")
graph.add_edge("Memory", "Finish")

current = "Planner"

print()

while current:

    print("Current Node:", current)

    current = graph.next_node(current)