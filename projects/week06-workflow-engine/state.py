class WorkflowState:
    """
    Shared state passed between every node in the workflow.
    """

    def __init__(self, user_input: str):

        self.user_input = user_input

        self.plan = []

        self.current_node = None

        self.tool = None

        self.memory = {}

        self.response = None

    def __repr__(self):

        return (
            f"WorkflowState("
            f"user_input={self.user_input!r}, "
            f"plan={self.plan}, "
            f"current_node={self.current_node}, "
            f"tool={self.tool}, "
            f"memory={self.memory}, "
            f"response={self.response!r})"
        )