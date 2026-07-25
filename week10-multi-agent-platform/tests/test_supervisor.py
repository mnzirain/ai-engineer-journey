from planner.enterprise_planner import EnterprisePlanner


def test_greeting_route():
    planner = EnterprisePlanner()
    assert planner.select_workflow("hello") == "greeting"


def test_calculator_route():
    planner = EnterprisePlanner()
    assert planner.select_workflow("10 + 5") == "calculator"


def test_translation_route():
    planner = EnterprisePlanner()
    assert planner.select_workflow("translate hello") == "translation"


def test_memory_route():
    planner = EnterprisePlanner()
    assert planner.select_workflow("remember my name") == "memory"