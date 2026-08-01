from registry.tool_registry import ToolRegistry


class ToolRouter:
    """
    Enterprise Tool Router

    Determines which enterprise tool should handle
    the user's request.
    """

    def __init__(self):

        self.registry = ToolRegistry()

    def route(self, query: str):

        q = query.lower()

        # Translation requests
        if "translate" in q:

            return self.registry.get("translate")

        # Summarization requests
        if "summarize" in q:

            return self.registry.get("summarize")

        # Default

        return self.registry.get("search")