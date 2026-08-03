from services.memory_service import MemoryService
from services.retrieval_service import RetrievalService


def test_retrieval():

    MemoryService.clear()

    MemoryService.remember("user_name", "Mike")

    result = RetrievalService.retrieve("user_name")

    assert result["user_name"] == "Mike"