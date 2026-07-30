from registry.service_registry import ServiceRegistry


class EnterpriseAIOrchestrator:

    def __init__(self):
        self.registry = ServiceRegistry()

    def process(self, query: str):

        q = query.lower()

        # Translation workflow
        if "translate" in q:

            summary = self.registry.summarizer.summarize(query)

            translation = self.registry.translator.translate(summary)

            return {
                "task": "translation",
                "query": query,
                "summary": summary,
                "translation": translation
            }

        # Summarization workflow
        if "summarize" in q or len(query.split()) > 25:

            summary = self.registry.summarizer.summarize(query)

            return {
                "task": "summarization",
                "query": query,
                "summary": summary
            }

        # Default: semantic search
        results = self.registry.search.search(query)

        return {
            "task": "semantic_search",
            "query": query,
            "results": results
        }