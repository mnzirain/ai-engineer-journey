from agents.base_agent import BaseAgent
from state import WorkflowState


class CalculatorAgent(BaseAgent):

    def __init__(self):

        super().__init__("Calculator Agent")

    def run(self, state: WorkflowState) -> WorkflowState:

        try:

            result = eval(state.user_input)

            state.response = f"The answer is {result}."

        except Exception:

            state.response = "Invalid calculation."

        return state