import secrets
import time


class JWTManager:

    def create_access_token(self, username):

        return {
            "token": secrets.token_hex(32),
            "user": username,
            "expires_in": 3600,
            "created": int(time.time())
        }

    def create_refresh_token(self, username):

        return {
            "token": secrets.token_hex(48),
            "user": username,
            "expires_in": 604800,
            "created": int(time.time())
        }