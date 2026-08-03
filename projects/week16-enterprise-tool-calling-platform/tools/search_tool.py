class SearchTool:

    name = "search"

    description = (
        "Searches the enterprise knowledge base using semantic search."
    )

    version = "1.0"

    input_schema = {
        "query": "string"
    }

    output_schema = {
        "results": "list"
    }

    def execute(self, query):

        return {
            "tool": self.name,
            "message": f"Searching knowledge base for '{query}'"
        }