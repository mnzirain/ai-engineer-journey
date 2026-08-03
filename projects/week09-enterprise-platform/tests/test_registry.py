from registry.workflow_registry import WorkflowRegistry


def test_greeting_exists():
    assert WorkflowRegistry.get_workflow("greeting") is not None


def test_calculator_exists():
    assert WorkflowRegistry.get_workflow("calculator") is not None


def test_memory_exists():
    assert WorkflowRegistry.get_workflow("memory") is not None