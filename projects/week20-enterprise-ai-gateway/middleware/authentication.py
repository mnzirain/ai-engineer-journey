from fastapi import Header, HTTPException


class AuthenticationMiddleware:

    VALID_KEYS = {
        "gateway-admin": "admin",
        "gateway-user": "user"
    }

    @classmethod
    def authenticate(cls, api_key: str):
        if api_key not in cls.VALID_KEYS:
            raise HTTPException(
                status_code=401,
                detail="Invalid API Key"
            )

        return cls.VALID_KEYS[api_key]