class Monitoring:

    metrics = {
        "requests": 0,
        "failures": 0
    }

    @classmethod
    def request(cls):

        cls.metrics["requests"] += 1

    @classmethod
    def failure(cls):

        cls.metrics["failures"] += 1

    @classmethod
    def get(cls):

        return cls.metrics