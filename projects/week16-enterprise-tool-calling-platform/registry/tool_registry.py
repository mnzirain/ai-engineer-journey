from tools.search_tool import SearchTool
from tools.summarizer_tool import SummarizerTool
from tools.translator_tool import TranslatorTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "search": SearchTool(),
            "summarize": SummarizerTool(),
            "translate": TranslatorTool(),
        }

    def get(self, tool_name):

        return self.tools.get(tool_name)

    def list_tools(self):

        return list(self.tools.keys())

    def describe_tools(self):

        descriptions = []

        for tool in self.tools.values():

            descriptions.append({

                "name": tool.name,

                "description": tool.description,

                "version": tool.version,

                "input": tool.input_schema,

                "output": tool.output_schema

            })

        return descriptions