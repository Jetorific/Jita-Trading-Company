from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from typing import Optional

class OAuthState:
    def __init__(self):
        self.expected_state: str = ""
        self.code: Optional[str] = None
        self.state: Optional[str] = None
        self.done: bool = False

# 1. Subclass HTTPServer to formally declare the attribute for Pylance
class OAuthHTTPServer(HTTPServer):
    oauth_state: OAuthState

class CallbackHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        code_list = params.get("code", [])
        state_list = params.get("state", [])

        if not code_list or not state_list:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing code or state")
            return

        code = code_list[0]
        state = state_list[0]

        # 2. Access the state via self.server
        # We use a cast or just ignore the type warning on self.server for strict checkers
        server = self.server  # type: OAuthHTTPServer
        
        if state != server.oauth_state.expected_state:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid state")
            return

        server.oauth_state.code = code
        server.oauth_state.state = state
        server.oauth_state.done = True

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Authorization complete. You can close this window.")