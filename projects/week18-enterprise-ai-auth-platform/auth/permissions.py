from auth.roles import Roles

ROLE_PERMISSIONS = {

    Roles.ADMIN: [
        "search",
        "summarize",
        "translate",
        "manage_users",
        "system_status"
    ],

    Roles.DOCTOR: [
        "search",
        "summarize",
        "translate"
    ],

    Roles.NURSE: [
        "search",
        "summarize"
    ],

    Roles.GUEST: [
        "search"
    ]

}


class PermissionManager:

    def has_permission(self, role: str, tool: str):

        permissions = ROLE_PERMISSIONS.get(role, [])

        return tool in permissions