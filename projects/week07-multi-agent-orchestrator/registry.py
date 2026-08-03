import importlib
import inspect
import pkgutil

from agents.base_agent import BaseAgent

from tools.calculator_tool import CalculatorTool
from tools.memory_tool import MemoryTool


class AgentManager:
    """
    Automatically discovers and loads every AI agent
    found inside the agents package.
    """

    def __init__(self):

        self.agents = {}

        self.load_agents()

    def load_agents(self):

        import agents

        for _, module_name, _ in pkgutil.iter_modules(agents.__path__):

            # Skip the abstract base class
            if module_name == "base_agent":
                continue

            module = importlib.import_module(f"agents.{module_name}")

            for _, obj in inspect.getmembers(module, inspect.isclass):

                if issubclass(obj, BaseAgent) and obj != BaseAgent:

                    self.agents[obj.__name__] = obj()

    def get_agent(self, name):

        return self.agents.get(name)

    def list_agents(self):

        return list(self.agents.keys())


class ToolRegistry:
    """
    Central registry for every tool used by the AI system.
    """

    def __init__(self):

        self.tools = {

            "calculator": CalculatorTool(),

            "memory": MemoryTool(),

        }

    def get_tool(self, tool_name):

        return self.tools.get(tool_name)

    def list_tools(self):

        return list(self.tools.keys())