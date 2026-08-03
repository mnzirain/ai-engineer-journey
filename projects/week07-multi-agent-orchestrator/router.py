class Router:
    """
    Chooses which agent should execute the plan.
    """

    def route(self, plan):

        task = plan[0]

        routes = {
            "greeting": "GreetingAgent",
            "calculator": "CalculatorAgent",
            "memory_store": "MemoryAgent",
            "memory_retrieve": "MemoryAgent",
            "knowledge": "KnowledgeAgent",
        }

        return routes.get(task, "KnowledgeAgent")