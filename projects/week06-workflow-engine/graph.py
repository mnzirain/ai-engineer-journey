class WorkflowGraph:

    def __init__(self):

        self.graph = {}

    def add_edge(self, source, destination):

        self.graph.setdefault(source, []).append(destination)

    def next_node(self, current):

        children = self.graph.get(current, [])

        if children:

            return children[0]

        return None

    def clear(self):

        self.graph = {}

    def display(self):

        print()

        print("Workflow Graph")

        print("----------------")

        for node, children in self.graph.items():

            print(f"{node} -> {children}")

        print()