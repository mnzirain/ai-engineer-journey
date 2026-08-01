class ResponseBuilder:
    """
    Enterprise Response Builder

    Produces a consistent response structure.
    """

    def build(self, tool_name, result):

        return {
            "tool": tool_name,
            "status": "success",
            "result": result
        }