from abc import ABC, abstractmethod

from state import WorkflowState


class BaseNode(ABC):
    """
    Base class for every workflow node.
    """

    @abstractmethod
    def run(self, state: WorkflowState) -> WorkflowState:
        """
        Execute the workflow node.
        """
        pass