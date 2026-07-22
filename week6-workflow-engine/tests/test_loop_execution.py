import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph import WorkflowGraph

graph = WorkflowGraph()

graph.add_edge("Planner", "Greeting")
graph.add_edge("Greeting", "MemoryStore")
graph.add_edge("MemoryStore", "Finish")

current = "Planner"

print()

while current:

    print("Current Node:", current)

    current = graph.next_node(current)