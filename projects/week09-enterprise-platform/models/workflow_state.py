from langgraph.graph import MessagesState


class WorkflowState(MessagesState):
    """
    Enterprise shared workflow state.
    """

    route: str