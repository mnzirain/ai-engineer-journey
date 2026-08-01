class ToolExecutor:
    """
    Enterprise Tool Executor

    Responsible for executing the selected tool.
    """

    def execute(self, tool, query):

        if tool is None:

            return {
                "error": "No tool selected."
            }

        return tool.execute(query)