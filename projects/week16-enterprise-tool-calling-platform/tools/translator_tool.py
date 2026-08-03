class TranslatorTool:

    name = "translate"

    description = (
        "Translates enterprise knowledge."
    )

    version = "1.0"

    input_schema = {
        "text": "string"
    }

    output_schema = {
        "translation": "string"
    }

    def execute(self, text):

        return {
            "tool": self.name,
            "message": f"Translating '{text}'"
        }