from abc import ABC, abstractmethod

from state import WorkflowState


class BaseAgent(ABC):
    """
    Base class for every AI agent.
    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def run(self, state: WorkflowState) -> WorkflowState:
        """
        Executes the agent.
        """
        pass