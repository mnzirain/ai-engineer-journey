import uuid

from core.security_engine import SecurityEngine
from core.request_router import RequestRouter


class MCPServer:

    def __init__(self):

        self.security = SecurityEngine()

        self.router = RequestRouter()

    def process(self, request):

        auth = self.security.authorize(
            request.api_key,
            request.tool
        )

        if not auth["authorized"]:

            return {
                "session_id": str(uuid.uuid4()),
                "status": "failed",
                "reason": auth["reason"]
            }

        result = self.router.execute(
            request.tool,
            request.payload
        )

        return {
            "session_id": str(uuid.uuid4()),
            "status": "success",
            "user": auth["username"],
            "role": auth["role"],
            "tool": request.tool,
            "output": result,
            "metadata": {
                "protocol": "MCP",
                "version": "1.0"
            }
        }