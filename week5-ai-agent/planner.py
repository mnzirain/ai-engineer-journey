class Planner:
    """
    Produces a sequence of actions for the Agent.
    """

    def plan(self, message: str):

        text = message.lower()

        # Memory questions

        if text == "what is my name?":
            return ["memory"]

        # Store name

        if text.startswith("my name is"):
            return ["memory_store"]

        # Greeting

        if text in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        ]:
            return ["greeting"]

        # Calculator

        if any(op in text for op in ["+", "-", "*", "/"]):
            return ["calculator"]

        if any(word in text for word in [
            "calculate",
            "add",
            "subtract",
            "multiply",
            "divide",
        ]):
            return ["calculator"]

        return ["llm"]