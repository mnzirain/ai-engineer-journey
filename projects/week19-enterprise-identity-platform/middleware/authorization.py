from auth.permissions import PERMISSIONS


class AuthorizationMiddleware:

    def authorize(self, role, action):

        if role not in PERMISSIONS:
            return False

        permissions = PERMISSIONS[role]

        if "*" in permissions:
            return True

        return action in permissions