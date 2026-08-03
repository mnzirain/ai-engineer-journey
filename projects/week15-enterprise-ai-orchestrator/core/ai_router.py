class AIRouter:

    def route(self, query: str):

        q = query.lower()

        if "translate" in q:
            return "translate"

        if "summarize" in q:
            return "summarize"

        return "search"