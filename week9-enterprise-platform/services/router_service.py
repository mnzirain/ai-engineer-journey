from registry.workflow_registry import WorkflowRegistry


class RouterService:
    """
    Executes the workflow selected by the Enterprise Planner.
    """

    @staticmethod
    def execute(route, state):
        workflow = WorkflowRegistry.get_workflow(route)

        if workflow is None:
            raise ValueError(f"No workflow registered for '{route}'")

        return workflow.invoke(state)