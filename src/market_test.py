import requests
import json
# need requests for making ESI API calls
# need json to save market data to file


def read_player_id():
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

'''
pulls player id from file in same directory
can be found in game as part of the url copied by right clicking your character name
'''

def read_auth_token():
    with open("auth.tok", "r") as f:
        auth_tok = f.read()
    return auth_tok

'''
PLEASE FOR THE LOVE OF GOD REMEMBER TO MAKE THIS USE OAUTH
WE CANNOT BE RE-VERIFYING EVERY 20 MINUTES
'''

def save_market_data(data):
    with open("src/data/market_data.json", "w") as f:
        json.dump(data, f, indent=2)

# Parses json return and writes to file, probably need to do more post processing later

url = "https://esi.evetech.net/markets/prices"

headers = {
    "Accept-Language": "en",
    "If-None-Match": "",
    "X-Compatibility-Date": "2026-07-21",
    "X-Tenant": "",
    "If-Modified-Since": "",
    "Accept": "application/json"
}

# Check the X-Compatability-Date, might need to be updated if script isn't working

response = requests.get(url, headers=headers)

save_market_data(response.json())

