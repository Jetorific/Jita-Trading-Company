import secrets
import webbrowser
import requests
import base64
import json
import time
from datetime import datetime

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

# --- Configuration ---
def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config("config.json")
CLIENT_ID = config["client_id"]
CLIENT_SECRET = config["client_secret"]
REDIRECT_URI = "http://localhost:8080/callback"
SCOPES = config["scopes"]

AUTH_URL = "https://login.eveonline.com/v2/oauth/authorize"
TOKEN_URL = "https://login.eveonline.com/v2/oauth/token"


def build_auth_url(state: str) -> str:
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "state": state,
    }
    query = urllib.parse.urlencode(params)
    return f"{AUTH_URL}?{query}"


def exchange_code_for_tokens(code: str) -> dict:
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}".encode("utf-8")
    basic_auth = base64.b64encode(credentials).decode("utf-8")

    headers = {
        "Authorization": f"Basic {basic_auth}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
    }

    resp = requests.post(TOKEN_URL, headers=headers, data=data)
    print("Token endpoint status:", resp.status_code)
    print("Token endpoint response:", resp.text)
    resp.raise_for_status()
    return resp.json()

def run_oauth_flow():
    oauth_state = OAuthState()

    # Generate state
    state = secrets.token_urlsafe(16)
    oauth_state.expected_state = state

    # Build and open authorize URL
    auth_url = build_auth_url(state)
    print("Opening browser for EVE login...")
    webbrowser.open(auth_url)

    server = OAuthHTTPServer(("localhost", 8080), CallbackHandler)
    server.oauth_state = oauth_state  # Set it on the server before starting


    # Wait until callback sets done=True
    while not oauth_state.done:
        server.handle_request()
        time.sleep(0.01)

    code = oauth_state.code
    if code is None:
        raise RuntimeError("Authorization code is still None after callback")

    tokens = exchange_code_for_tokens(code)
    tokens['date_issued'] = datetime.now().isoformat()
    with open("auth_tokens.json", "w") as f:
            json.dump(tokens, f, indent=2)
    
    print("\n=== Tokens ===")
    print("Access token: ", tokens["access_token"])
    print("Refresh token:", tokens["refresh_token"])
    print("Expires in:   ", tokens["expires_in"])
    return tokens


if __name__ == "__main__":
    run_oauth_flow()