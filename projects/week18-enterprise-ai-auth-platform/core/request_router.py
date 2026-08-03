class RequestRouter:

    def execute(self, tool: str, payload: dict):

        if tool == "search":
            return {
                "tool": tool,
                "message": f"Searching enterprise knowledge for '{payload.get('query', '')}'"
            }

        if tool == "summarize":
            return {
                "tool": tool,
                "message": f"Summarizing '{payload.get('text', '')}'"
            }

        if tool == "translate":
            return {
                "tool": tool,
                "message": f"Translating '{payload.get('text', '')}'"
            }

        return {
            "tool": tool,
            "message": "Unknown enterprise tool."
        }