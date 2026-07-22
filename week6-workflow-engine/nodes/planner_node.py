from nodes.base_node import BaseNode
from planner import Planner


class PlannerNode(BaseNode):

    name = "Planner"

    def __init__(self):

        self.planner = Planner()

    def run(self, state):

        state.plan = self.planner.plan(state.user_input)

        return state