class ToolRegistry:
    """
    Enterprise MCP Tool Registry
    """

    def __init__(self):
        self.tools = {
            "search": {
                "description": "Enterprise semantic search"
            },
            "summarize": {
                "description": "Enterprise summarization"
            },
            "translate": {
                "description": "Enterprise translation"
            }
        }

    def get_tools(self):
        return self.tools

    def get_tool(self, tool_name):
        return self.tools.get(tool_name)