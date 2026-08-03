import requests
import json

def read_player_id():
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

def read_auth_token():
    with open("auth.tok", "r") as f:
        auth_tok = f.read()
    return auth_tok

import requests

player_id = read_player_id()
auth_tok = read_auth_token()

url = f"https://esi.evetech.net/characters/{player_id}/location"

headers = {
    "Accept-Language": "en",
    "If-None-Match": "",
    "X-Compatibility-Date": "2026-07-21",
    "X-Tenant": "",
    "If-Modified-Since": "",
    "Accept": "application/json",
    "Authorization": auth_tok
}

response = requests.get(url, headers=headers)

print(response.json())