class RateLimiter:

    requests = {}

    # Change temporarily to 2 for screenshot demonstration
    LIMIT = 2

    @classmethod
    def check(cls, api_key):

        cls.requests.setdefault(api_key, 0)

        cls.requests[api_key] += 1

        if cls.requests[api_key] > cls.LIMIT:
            return False

        return True