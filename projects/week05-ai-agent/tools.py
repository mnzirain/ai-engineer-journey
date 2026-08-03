import re


class CalculatorTool:
    """
    Performs arithmetic calculations.
    """

    name = "calculator"

    def execute(self, expression: str) -> str:
        try:
            expression = expression.lower()

            # Remove everything except numbers and math operators
            expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)

            expression = expression.strip()

            result = eval(expression)

            return str(result)

        except Exception:
            return "Invalid calculation."


class GreetingTool:
    """
    Returns friendly greetings.
    """

    name = "greeting"

    def execute(self, message: str = "") -> str:
        return "Hello! How can I help you today?"