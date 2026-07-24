from services.router_service import RouterService


def test_router_exists():
    assert RouterService is not None


def test_execute_function_exists():
    assert hasattr(RouterService, "execute")