from auth.api_keys import API_KEYS
from models.auth_models import AuthResult


class AuthenticationManager:

    def authenticate(self, api_key: str):

        if api_key in API_KEYS:

            user = API_KEYS[api_key]

            return AuthResult(
                authenticated=True,
                username=user["username"],
                role=user["role"]
            )

        return AuthResult(
            authenticated=False,
            username="",
            role=""
        )