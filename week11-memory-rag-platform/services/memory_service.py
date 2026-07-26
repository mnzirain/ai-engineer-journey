from memory.memory_store import MemoryStore


class MemoryService:
    """
    Enterprise Memory Service

    Handles all memory operations for
    every agent in the platform.
    """

    @staticmethod
    def remember(key, value):
        MemoryStore.save(key, value)

    @staticmethod
    def recall(key):
        return MemoryStore.load(key)

    @staticmethod
    def show_memory():
        return MemoryStore.all()

    @staticmethod
    def clear():
        MemoryStore.clear()