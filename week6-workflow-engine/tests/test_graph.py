import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from graph import WorkflowGraph

graph = WorkflowGraph()

graph.add_edge("Planner", "Greeting")
graph.add_edge("Planner", "Calculator")
graph.add_edge("Planner", "Memory")

graph.add_edge("Greeting", "Finish")
graph.add_edge("Calculator", "Finish")
graph.add_edge("Memory", "Finish")

graph.display()

print()

print("Next after Planner:", graph.next_nodes("Planner"))

print("Next after Greeting:", graph.next_nodes("Greeting"))

print("Next after Memory:", graph.next_nodes("Memory"))