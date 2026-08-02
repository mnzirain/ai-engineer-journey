import secrets


class RefreshTokenManager:

    def __init__(self):
        self.tokens = {}

    def issue(self, username):

        token = secrets.token_hex(48)

        self.tokens[token] = username

        return token

    def validate(self, token):

        return token in self.tokens

    def owner(self, token):

        return self.tokens.get(token)

    def revoke(self, token):

        if token in self.tokens:
            del self.tokens[token]