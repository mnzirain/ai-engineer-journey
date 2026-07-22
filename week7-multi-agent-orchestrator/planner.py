class Planner:
    """
    Creates an ordered workflow plan.
    """

    def create_plan(self, state):

        message = state.user_input.lower()

        plan = []

        if "hello" in message or "hi" in message:
            plan.append("greeting")

        if "my name is" in message:
            plan.append("memory_store")

        if "what is my name" in message:
            plan.append("memory_retrieve")

        if "+" in message:
            plan.append("calculator")

        if not plan:
            plan.append("knowledge")

        state.plan = plan

        return state