class AgentMemory:
    """
    Stores simple facts about the conversation.
    """

    def __init__(self):

        self.data = {}

    def remember_name(self, message: str):

        text = message.strip()

        if text.lower().startswith("my name is"):

            name = text[10:].strip()

            self.data["name"] = name

            return True

        return False

    def get_name(self):

        return self.data.get("name")