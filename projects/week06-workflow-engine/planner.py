class Planner:
    """
    Simple workflow planner.
    Decides which workflow should execute.
    """

    def plan(self, message: str):

        message = message.lower()

        if "my name is" in message:
            return ["memory_store"]

        if "what is my name" in message:
            return ["memory"]

        if any(op in message for op in ["+", "-", "*", "/"]) or "calculate" in message:
            return ["calculator"]

        return ["greeting"]