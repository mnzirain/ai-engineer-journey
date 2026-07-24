import importlib

WORKFLOW_MODULES = {
    "greeting": "graphs.greeting_graph",
    "calculator": "graphs.calculator_graph",
    "knowledge": "graphs.knowledge_graph",
    "translation": "graphs.translation_graph",
    "memory": "graphs.memory_graph",
}


def load_graph(workflow_name):
    module_name = WORKFLOW_MODULES.get(workflow_name)

    if module_name is None:
        return None

    module = importlib.import_module(module_name)

    return getattr(module, f"{workflow_name}_graph", None)