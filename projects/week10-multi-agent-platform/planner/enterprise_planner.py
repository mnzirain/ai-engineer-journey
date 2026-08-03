class EnterprisePlanner:
    """
    Enterprise Planner

    Determines which specialist agent
    should execute the user's request.
    """

    def select_workflow(self, user_input: str):

        text = user_input.lower()

        print(f"\nPlanner received: {text}")

        if "translate" in text:
            route = "translation"

        elif "remember" in text:
            route = "memory"

        elif any(op in text for op in ["+", "-", "*", "/"]):
            route = "calculator"

        elif any(
            word in text
            for word in [
                "what",
                "who",
                "where",
                "when",
                "why",
                "artificial",
                "intelligence",
            ]
        ):
            route = "knowledge"

        else:
            route = "greeting"

        print(f"Selected workflow: {route}")

        return route