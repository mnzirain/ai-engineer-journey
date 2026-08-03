class EnterprisePlanner:

    """
    Enterprise Planner

    Responsible only for deciding
    which workflow should execute.
    """

    def classify(self, user_input: str):

        message = user_input.lower()

        if any(word in message for word in ["hello", "hi", "hey"]):
            return "greeting"

        elif any(symbol in message for symbol in ["+", "-", "*", "/"]):
            return "calculator"

        elif "remember" in message or "my name" in message:
            return "memory"

        else:
            return "knowledge"