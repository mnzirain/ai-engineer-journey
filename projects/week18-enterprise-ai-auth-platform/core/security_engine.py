from auth.auth_manager import AuthenticationManager
from auth.permissions import PermissionManager


class SecurityEngine:

    def __init__(self):
        self.auth = AuthenticationManager()
        self.permissions = PermissionManager()

    def authorize(self, api_key: str, tool: str):

        auth_result = self.auth.authenticate(api_key)

        if not auth_result.authenticated:
            return {
                "authorized": False,
                "reason": "Invalid API Key"
            }

        allowed = self.permissions.has_permission(
            auth_result.role,
            tool
        )

        if not allowed:
            return {
                "authorized": False,
                "reason": "Permission denied"
            }

        return {
            "authorized": True,
            "username": auth_result.username,
            "role": auth_result.role
        }