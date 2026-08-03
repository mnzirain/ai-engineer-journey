class ResponseBuilder:

    @staticmethod
    def build(task, query, results=None, summary=None, translation=None):

        response = {

            "task": task,

            "query": query

        }

        if results is not None:
            response["results"] = results

        if summary is not None:
            response["summary"] = summary

        if translation is not None:
            response["translation"] = translation

        return response