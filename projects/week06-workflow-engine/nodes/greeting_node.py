from nodes.base_node import BaseNode
from state import WorkflowState


class GreetingNode(BaseNode):

    name = "Greeting"

    def run(self, state: WorkflowState) -> WorkflowState:

        state.response = "Hello! How can I help you today?"

        return state