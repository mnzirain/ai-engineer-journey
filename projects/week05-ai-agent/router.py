import re


class Router:
    """
    Routes user requests to the appropriate tool.
    """

    def route(self, message: str) -> str:

        text = message.lower().strip()

        greetings = [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        ]

        if text in greetings:
            return "greeting"

        calculation_keywords = [
            "calculate",
            "add",
            "subtract",
            "multiply",
            "divide",
        ]

        if any(word in text for word in calculation_keywords):
            return "calculator"

        if re.fullmatch(r"[0-9\+\-\*\/\(\)\.\s]+", text):
            return "calculator"

        return "llm"