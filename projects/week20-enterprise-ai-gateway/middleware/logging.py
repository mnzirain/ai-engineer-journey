from datetime import datetime


class LoggingMiddleware:

    @staticmethod
    def log(endpoint, provider):

        print(
            f"[{datetime.now()}] "
            f"Endpoint={endpoint} "
            f"Provider={provider}"
        )