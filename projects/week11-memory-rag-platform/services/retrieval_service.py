from retriever.retriever import Retriever


class RetrievalService:
    """
    Enterprise Retrieval Service

    Used by all agents to retrieve
    information from memory.
    """

    @staticmethod
    def retrieve(query):

        return Retriever.search(query)