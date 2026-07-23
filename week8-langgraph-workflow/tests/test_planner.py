from services.planner_service import EnterprisePlanner


def test_greeting():

    planner = EnterprisePlanner()

    assert planner.classify("Hello Mike") == "greeting"


def test_calculator():

    planner = EnterprisePlanner()

    assert planner.classify("10 + 20") == "calculator"


def test_knowledge():

    planner = EnterprisePlanner()

    assert planner.classify("Explain AI") == "knowledge"