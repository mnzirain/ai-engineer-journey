from dataclasses import dataclass, field


@dataclass
class WorkflowState:
    """
    Shared state for the entire AI orchestration system.
    """

    user_input: str = ""

    plan: list = field(default_factory=list)

    selected_agent: str = ""

    selected_tool: str = ""

    memory: dict = field(default_factory=dict)

    response: str = ""