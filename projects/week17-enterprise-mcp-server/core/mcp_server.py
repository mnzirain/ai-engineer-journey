from core.context_manager import ContextManager
from core.session_manager import SessionManager
from registry.tool_registry import ToolRegistry
from core.mcp_response import MCPResponse


class MCPServer:
    """
    Enterprise Model Context Protocol (MCP) Server

    Responsibilities:
    - Session management
    - Context management
    - Tool discovery
    - Tool invocation
    - Standardized responses
    """

    def __init__(self):

        self.sessions = SessionManager()

        self.context = ContextManager()

        self.registry = ToolRegistry()

    def list_tools(self):

        return self.registry.get_tools()

    def invoke(self, tool_name: str, input_data: dict):

        session_id = self.sessions.create_session()

        self.context.save(
            session_id,
            "last_tool",
            tool_name
        )

        if tool_name == "search":

            result = {
                "message": f"Searching enterprise knowledge for '{input_data.get('query','')}'"
            }

        elif tool_name == "summarize":

            result = {
                "message": f"Summarizing '{input_data.get('text','')}'"
            }

        elif tool_name == "translate":

            result = {
                "message": f"Translating '{input_data.get('text','')}'"
            }

        else:

            result = {
                "message": "Unknown enterprise tool."
            }

        return MCPResponse(
            session_id=session_id,
            tool=tool_name,
            status="success",
            output=result,
            metadata={
                "protocol": "MCP",
                "version": "1.0"
            }
        )