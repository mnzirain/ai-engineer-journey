from registry.graph_loader import load_graph


class WorkflowRegistry:
    """
    Enterprise Workflow Registry
    Dynamically loads workflows.
    """

    @classmethod
    def get_workflow(cls, workflow_name):
        return load_graph(workflow_name)