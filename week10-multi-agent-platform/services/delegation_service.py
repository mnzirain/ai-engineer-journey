class DelegationService:
    """
    Chooses which specialist agent
    should handle the request.
    """

    @staticmethod
    def select(user_input: str):

        text = user_input.lower()

        if "translate" in text:
            return "translation"

        elif "remember" in text:
            return "memory"

        elif any(op in text for op in ["+", "-", "*", "/"]):
            return "calculator"

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
            return "knowledge"

        return "greeting"