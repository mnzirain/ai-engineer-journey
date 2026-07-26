from services.retrieval_service import RetrievalService


def test_retrieval():

    results = RetrievalService.search(
        "Explain Retrieval-Augmented Generation"
    )

    assert len(results) > 0