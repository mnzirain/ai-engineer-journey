import uuid
import time


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create_session(self, username):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "username": username,
            "created": int(time.time())
        }

        return session_id

    def get_session(self, session_id):

        return self.sessions.get(session_id)

    def destroy_session(self, session_id):

        if session_id in self.sessions:
            del self.sessions[session_id]