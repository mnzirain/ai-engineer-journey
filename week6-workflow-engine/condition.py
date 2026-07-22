class Condition:

    """
    Decides which node should execute.
    """

    def evaluate(self, state):

        if not state.plan:
            return None

        return state.plan[0]