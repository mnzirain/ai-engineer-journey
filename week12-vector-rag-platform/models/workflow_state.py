from typing import TypedDict, List


class WorkflowState(TypedDict):
    """
    Shared workflow state.
    """

    query: str

    documents: List[str]

    embeddings: list

    results: List[str]