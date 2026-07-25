from services.delegation_service import DelegationService


class SupervisorAgent:
    """
    Enterprise Supervisor Agent

    Responsible for delegating user requests
    to the appropriate specialist workflow.
    """

    @staticmethod
    def delegate(user_input: str):

        route = DelegationService.select(user_input)

        print(f"\nSupervisor selected -> {route}")

        return route