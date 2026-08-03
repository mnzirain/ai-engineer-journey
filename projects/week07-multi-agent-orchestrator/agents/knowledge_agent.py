from agents.base_agent import BaseAgent
from state import WorkflowState


class KnowledgeAgent(BaseAgent):

    def __init__(self):

        super().__init__("Knowledge Agent")

    def run(self, state: WorkflowState) -> WorkflowState:

        state.response = "Knowledge Agent executed."

        return state