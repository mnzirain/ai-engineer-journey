from security.token_validation import TokenValidator


class AuthenticationMiddleware:

    def __init__(self):
        self.validator = TokenValidator()

    def authenticate(self, token):

        if not self.validator.validate(token):
            return {
                "authenticated": False,
                "reason": "Invalid or missing access token."
            }

        return {
            "authenticated": True
        }