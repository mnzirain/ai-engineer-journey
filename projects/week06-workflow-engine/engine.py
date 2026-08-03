from graph import WorkflowGraph
from condition import Condition
from state import WorkflowState

from nodes.planner_node import PlannerNode
from nodes.greeting_node import GreetingNode
from nodes.calculator_node import CalculatorNode
from nodes.memory_store_node import MemoryStoreNode
from nodes.memory_retrieve_node import MemoryRetrieveNode


class WorkflowEngine:

    def __init__(self):

        self.state = WorkflowState("")

        self.graph = WorkflowGraph()

        self.condition = Condition()

        self.planner = PlannerNode()

        self.nodes = {

            "Greeting": GreetingNode(),

            "Calculator": CalculatorNode(),

            "MemoryStore": MemoryStoreNode(),

            "MemoryRetrieve": MemoryRetrieveNode(),

        }

    def build_graph(self, decision):

        self.graph.clear()

        if decision == "greeting":

            self.graph.add_edge("Planner", "Greeting")
            self.graph.add_edge("Greeting", "Finish")

        elif decision == "calculator":

            self.graph.add_edge("Planner", "Calculator")
            self.graph.add_edge("Calculator", "Finish")

        elif decision == "memory_store":

            self.graph.add_edge("Planner", "MemoryStore")
            self.graph.add_edge("MemoryStore", "Finish")

        elif decision == "memory":

            self.graph.add_edge("Planner", "MemoryRetrieve")
            self.graph.add_edge("MemoryRetrieve", "Finish")

    def run(self, message: str):

        self.state.user_input = message

        self.state.response = None

        self.state = self.planner.run(self.state)

        print(f"[Planner] {self.state.plan}")

        decision = self.condition.evaluate(self.state)

        self.build_graph(decision)

        self.graph.display()

        current = "Planner"

        while current != "Finish":

            next_node = self.graph.next_node(current)

            if next_node is None:

                break

            if next_node in self.nodes:

                node = self.nodes[next_node]

                self.state = node.run(self.state)

            current = next_node

        return self.state