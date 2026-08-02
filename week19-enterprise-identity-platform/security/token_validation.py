class TokenValidator:

    def validate(self, token):

        if not token:
            return False

        if isinstance(token, dict):

            return "token" in token

        return False