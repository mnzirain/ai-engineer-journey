import re


class ContextBuilder:
    """
    Builds task-specific context for each AI agent.
    """

    def build(self, task: str, user_message: str):

        message = user_message.strip()

        if task == "greeting":

            return "Hello"

        elif task == "memory_store":

            match = re.search(
                r"my name is\s+([A-Za-z]+)",
                message,
                re.IGNORECASE,
            )

            if match:

                return match.group(1)

            return ""

        elif task == "memory_retrieve":

            return "What is my name?"

        elif task == "calculator":

            match = re.search(
                r"(\d+\s*[\+\-\*/]\s*\d+)",
                message,
            )

            if match:

                return match.group(1)

            return ""

        return message