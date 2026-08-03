from llm import get_llm
from planner import Planner
from router import Router
from registry import ToolRegistry
from memory import AgentMemory


class AIAgent:

    def __init__(self):

        self.memory = AgentMemory()

        self.planner = Planner()

        self.router = Router()

        self.registry = ToolRegistry()

        self.llm = get_llm()

        print("AI Agent initialized.")

    def chat(self, message: str) -> str:

        plan = self.planner.plan(message)

        print(f"[Planner] Plan: {plan}")

        final_answer = ""

        for step in plan:

            # Memory Store

            if step == "memory_store":

                self.memory.remember_name(message)

                final_answer = "Nice to meet you!"

                continue

            # Memory Retrieve

            if step == "memory":

                name = self.memory.get_name()

                if name:

                    final_answer = f"Your name is {name}."

                else:

                    final_answer = "I don't know your name yet."

                continue

            # Route

            tool_name = self.router.route(message)

            print(f"[Router] Selected tool: {tool_name}")

            tool = self.registry.get_tool(tool_name)

            if tool:

                result = tool.execute(message)

                if tool_name == "calculator":

                    final_answer = f"The answer is {result}."

                else:

                    final_answer = result

            else:

                final_answer = self.llm.generate(message)

        return final_answer