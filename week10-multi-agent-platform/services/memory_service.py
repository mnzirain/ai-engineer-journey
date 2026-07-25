class MemoryService:
    """
    Shared Memory Service

    Stores simple key-value information
    for all agents.
    """

    memory = {}

    @classmethod
    def save(cls, key, value):
        cls.memory[key] = value

    @classmethod
    def load(cls, key):
        return cls.memory.get(key)

    @classmethod
    def show(cls):
        return cls.memory