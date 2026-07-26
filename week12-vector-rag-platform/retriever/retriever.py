from services.retrieval_service import RetrievalService


class EnterpriseRetriever:
    """
    Enterprise Retrieval Wrapper
    """

    @staticmethod
    def retrieve(query):

        return RetrievalService.search(query)