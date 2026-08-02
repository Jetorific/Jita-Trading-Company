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

def save_market_data(data):
    with open("src/data/market_data.json", "w") as f:
        json.dump(data, f, indent=2)


url = "https://esi.evetech.net/markets/prices"

headers = {
    "Accept-Language": "en",
    "If-None-Match": "",
    "X-Compatibility-Date": "2026-07-21",
    "X-Tenant": "",
    "If-Modified-Since": "",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

save_market_data(response.json())

