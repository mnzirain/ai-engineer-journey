class OAuthManager:

    def __init__(self):

        # Enterprise demo users
        self.users = {
            "mike": "password123",
            "doctor": "doctor123",
            "guest": "guest123"
        }

    def authenticate(self, username, password):

        if username not in self.users:
            return False

        return self.users[username] == password