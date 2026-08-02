from auth.oauth import OAuthManager
from auth.jwt_manager import JWTManager
from auth.refresh_tokens import RefreshTokenManager

from security.hashing import HashingEngine

from core.session_manager import SessionManager


class IdentityServer:

    def __init__(self):

        self.oauth = OAuthManager()

        self.jwt = JWTManager()

        self.refresh = RefreshTokenManager()

        self.hashing = HashingEngine()

        self.sessions = SessionManager()

    def login(self, request):

        authenticated = self.oauth.authenticate(
            request.username,
            request.password
        )

        if not authenticated:

            return {
                "status": "failed",
                "message": "Invalid username or password."
            }

        access_token = self.jwt.create_access_token(
            request.username
        )

        refresh_token = self.refresh.issue(
            request.username
        )

        session = self.sessions.create_session(
            request.username
        )

        return {

            "status": "success",

            "username": request.username,

            "session_id": session,

            "access_token": access_token,

            "refresh_token": refresh_token,

            "token_type": "Bearer"

        }