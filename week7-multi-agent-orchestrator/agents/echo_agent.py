from agents.base_agent import BaseAgent


class EchoAgent(BaseAgent):

    def __init__(self):
        super().__init__("Echo Agent")

    def run(self, state):

        state.response = state.user_input

        return state