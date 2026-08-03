import secrets
import webbrowser
import requests
import base64
import json
import time
from datetime import datetime

from eve_oauth_callback import *

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