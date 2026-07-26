from planner.enterprise_planner import EnterprisePlanner


planner = EnterprisePlanner()


def test_greeting():

    assert planner.select_workflow("hello") == "greeting"


def test_memory():

    assert planner.select_workflow("remember my name") == "memory"


def test_retrieval():

    assert planner.select_workflow("what is my name") == "retrieval"


def test_calculator():

    assert planner.select_workflow("10 + 20") == "calculator"