import hashlib


class HashingEngine:

    def hash_password(self, password: str):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    def verify_password(self, password, hashed):

        return (
            self.hash_password(password)
            == hashed
        )