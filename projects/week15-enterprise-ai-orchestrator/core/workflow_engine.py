from registry.service_registry import ServiceRegistry
from core.ai_router import AIRouter
from core.response_builder import ResponseBuilder


class WorkflowEngine:

    def __init__(self):

        self.router = AIRouter()

        self.registry = ServiceRegistry()

    def process(self, query):

        task = self.router.route(query)

        # SEARCH ONLY
        if task == "search":

            results = self.registry.search.search(query)

            return ResponseBuilder.build(

                task="semantic_search",

                query=query,

                results=results

            )

        # SEARCH → SUMMARIZE
        if task == "summarize":

            results = self.registry.search.search(query)

            context = "\n\n".join(

                item["text"]

                for item in results

            )

            summary = self.registry.summarizer.summarize(context)

            return ResponseBuilder.build(

                task="search_then_summarize",

                query=query,

                results=results,

                summary=summary

            )

        # SEARCH → SUMMARIZE → TRANSLATE
        if task == "translate":

            results = self.registry.search.search(query)

            context = "\n\n".join(

                item["text"]

                for item in results

            )

            summary = self.registry.summarizer.summarize(context)

            translation = self.registry.translator.translate(summary)

            return ResponseBuilder.build(

                task="search_summarize_translate",

                query=query,

                results=results,

                summary=summary,

                translation=translation

            )