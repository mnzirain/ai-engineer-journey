from tools import CalculatorTool, GreetingTool


class ToolRegistry:
    """
    Stores and provides access to all available tools.
    """

    def __init__(self):

        self.tools = {
            "calculator": CalculatorTool(),
            "greeting": GreetingTool(),
        }

    def get_tool(self, name: str):

        return self.tools.get(name)