from graph import graph


class WorkflowRegistry:

    """
    Returns the workflow
    associated with the planner result.
    """

    def get(self, workflow_name):

        # For Week 8 we use one graph.
        # Later this becomes multiple graphs.

        return graph