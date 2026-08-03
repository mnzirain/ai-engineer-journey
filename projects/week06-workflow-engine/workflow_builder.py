from graph import WorkflowGraph


class WorkflowBuilder:
    """
    Builds a workflow graph dynamically
    based on the planner output.
    """

    def build(self, plan):

        graph = WorkflowGraph()

        previous = "Planner"

        for step in plan:

            mapping = {
                "greeting": "Greeting",
                "calculator": "Calculator",
                "memory_store": "MemoryStore",
                "memory": "MemoryRetrieve",
            }

            node = mapping.get(step)

            if node:

                graph.add_edge(previous, node)

                previous = node

        graph.add_edge(previous, "Finish")

        return graph