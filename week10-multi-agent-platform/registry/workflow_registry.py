from graphs.supervisor_graph import supervisor_graph


class WorkflowRegistry:
    """
    Week 10 Workflow Registry

    Returns the compiled Supervisor Graph.
    """

    @classmethod
    def get_graph(cls):
        return supervisor_graph