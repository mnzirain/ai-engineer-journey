class EnterprisePlanner:
    """
    Enterprise Planner

    Chooses which workflow should execute.
    """

    @staticmethod
    def select_workflow(user_input):

        text = user_input.lower()

        print(f"\nPlanner received: {text}")

        if "retrieval" in text or "vector" in text:
            route = "retrieval"
        else:
            route = "retrieval"

        print(f"Selected workflow: {route}")

        return route