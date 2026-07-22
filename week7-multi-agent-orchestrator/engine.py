from planner import Planner
from router import Router
from registry import AgentManager
from state import WorkflowState
from context_builder import ContextBuilder


class OrchestratorEngine:
    """
    Coordinates multiple AI agents using task-specific context.
    """

    def __init__(self):

        self.planner = Planner()
        self.router = Router()
        self.manager = AgentManager()
        self.context_builder = ContextBuilder()

    def run(self, user_message: str):

        state = WorkflowState(user_input=user_message)

        state = self.planner.create_plan(state)

        responses = []

        original_message = user_message

        for task in state.plan:

            state.user_input = self.context_builder.build(task, original_message)

            agent_name = self.router.route([task])

            agent = self.manager.get_agent(agent_name)

            state = agent.run(state)

            responses.append(state.response)

        state.user_input = original_message

        state.response = " | ".join(responses)

        return state