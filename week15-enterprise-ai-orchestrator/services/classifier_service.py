class ClassifierService:

    def classify(self, query: str):

        q = query.lower()

        # Translation requests
        if "translate" in q:
            return "translate"

        # Explicit summarization requests
        if "summarize" in q:
            return "summarize"

        # Long paragraphs should be summarized automatically
        if len(query.split()) > 25:
            return "summarize"

        # Everything else → semantic search
        return "search"