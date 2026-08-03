class EnterprisePlanner:
    """
    Enterprise AI Planner

    Chooses which specialist
    should handle the request.
    """

    def select_workflow(self, user_input: str):

        text = user_input.lower()

        print(f"\nPlanner received: {text}")

        if "remember" in text:

            workflow = "memory"

        elif "what is my name" in text:

            workflow = "retrieval"

        elif "translate" in text:

            workflow = "translation"

        elif "+" in text:

            workflow = "calculator"

        elif "what is" in text:

            workflow = "knowledge"

        else:

            workflow = "greeting"

        print(f"Selected workflow: {workflow}")

        return workflow