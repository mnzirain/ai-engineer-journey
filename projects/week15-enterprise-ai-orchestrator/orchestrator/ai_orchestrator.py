from registry.service_registry import ServiceRegistry


class EnterpriseAIOrchestrator:

    def __init__(self):
        self.registry = ServiceRegistry()

    def process(self, query: str):

        q = query.lower()

        # ---------------------------------------------------
        # SEARCH → SUMMARIZE → TRANSLATE
        # ---------------------------------------------------

        if "translate" in q:

            results = self.registry.search.search(query)

            context = "\n\n".join(
                item["text"] for item in results
            )

            summary = self.registry.summarizer.summarize(context)

            translation = self.registry.translator.translate(summary)

            return {

                "workflow": "search → summarize → translate",

                "query": query,

                "sources": results,

                "summary": summary,

                "translation": translation

            }

        # ---------------------------------------------------
        # SEARCH → SUMMARIZE
        # ---------------------------------------------------

        if "summarize" in q or len(query.split()) > 25:

            results = self.registry.search.search(query)

            context = "\n\n".join(
                item["text"] for item in results
            )

            summary = self.registry.summarizer.summarize(context)

            return {

                "workflow": "search → summarize",

                "query": query,

                "sources": results,

                "summary": summary

            }

        # ---------------------------------------------------
        # SEMANTIC SEARCH ONLY
        # ---------------------------------------------------

        results = self.registry.search.search(query)

        return {

            "workflow": "semantic search",

            "query": query,

            "results": results

        }