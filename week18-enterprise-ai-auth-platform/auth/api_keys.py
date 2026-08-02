from auth.roles import Roles


API_KEYS = {

    "admin-key-123": {
        "username": "mike",
        "role": Roles.ADMIN
    },

    "doctor-key-456": {
        "username": "doctor",
        "role": Roles.DOCTOR
    },

    "guest-key-789": {
        "username": "guest",
        "role": Roles.GUEST
    }

}