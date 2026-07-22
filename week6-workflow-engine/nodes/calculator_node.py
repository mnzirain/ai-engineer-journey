from nodes.base_node import BaseNode
from state import WorkflowState


class CalculatorNode(BaseNode):

    name = "Calculator"

    def run(self, state: WorkflowState) -> WorkflowState:

        try:

            expression = state.user_input.replace("calculate", "").strip()

            result = eval(expression)

            state.response = f"The answer is {result}."

        except Exception:

            state.response = "Invalid calculation."

        return state