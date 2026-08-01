class SummarizerTool:

    name = "summarize"

    description = (
        "Summarizes enterprise knowledge."
    )

    version = "1.0"

    input_schema = {
        "text": "string"
    }

    output_schema = {
        "summary": "string"
    }

    def execute(self, text):

        return {
            "tool": self.name,
            "message": f"Summarizing '{text}'"
        }