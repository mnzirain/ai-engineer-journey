from typing import TypedDict
from langchain_core.messages import BaseMessage


class WorkflowState(TypedDict):
    """
    Shared workflow state
    passed between agents.
    """

    messages: list[BaseMessage]
    route: str