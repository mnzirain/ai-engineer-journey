class MemoryStore:
    """
    Enterprise Shared Memory Store

    Provides shared memory for all agents.

    This simulates long-term memory and will
    later be upgraded to a real vector database.
    """

    _memory = {}

    @classmethod
    def save(cls, key: str, value: str):
        cls._memory[key] = value

    @classmethod
    def load(cls, key: str):
        return cls._memory.get(key)

    @classmethod
    def all(cls):
        return dict(cls._memory)

    @classmethod
    def clear(cls):
        cls._memory.clear()