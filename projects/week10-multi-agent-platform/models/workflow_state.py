from langgraph.graph import MessagesState


class WorkflowState(MessagesState):
    """
    Shared workflow state for the Enterprise Multi-Agent Platform.
    """

    route: str