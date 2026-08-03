class ContextBuilder:

    def build_context(self, retrieval_results):

        context = ""

        for result in retrieval_results:

            context += (
                f"\nSource: {result['filename']}\n"
                f"{result['text']}\n"
            )

        return context.strip()