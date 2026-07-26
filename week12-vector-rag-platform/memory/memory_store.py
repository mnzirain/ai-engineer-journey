"""
Enterprise Memory Store

Reserved for future conversational memory.
"""


class MemoryStore:

    def __init__(self):

        self.memory = []

    def add(self, item):

        self.memory.append(item)

    def get_all(self):

        return self.memory