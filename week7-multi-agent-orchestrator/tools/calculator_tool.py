class CalculatorTool:
    """
    Performs simple calculations.
    """

    def calculate(self, expression):

        try:
            return str(eval(expression))

        except Exception:
            return "Calculation Error"