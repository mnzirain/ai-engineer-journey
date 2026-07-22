import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from workflow_builder import WorkflowBuilder

builder = WorkflowBuilder()

plans = [

    ["greeting"],

    ["calculator"],

    ["memory_store"],

    ["memory"],

]

for plan in plans:

    graph = builder.build(plan)

    print()

    print("Plan:", plan)

    graph.display()