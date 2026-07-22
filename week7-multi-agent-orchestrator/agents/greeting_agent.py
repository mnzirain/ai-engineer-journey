from agents.base_agent import BaseAgent
from state import WorkflowState


class GreetingAgent(BaseAgent):

    def __init__(self):

        super().__init__("Greeting Agent")

    def run(self, state: WorkflowState) -> WorkflowState:

        state.response = "Hello! How can I help you today?"

        return state