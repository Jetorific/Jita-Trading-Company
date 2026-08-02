import requests

def get_wallet_balance(vars):
    url = f"https://esi.evetech.net/characters/{vars['player_id']}/wallet"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": vars["compatibility_date"],
        "X-Tenant": "",
        "If-Modified-Since": "",
        "Accept": "application/json",
        "Authorization": vars["auth_token"]
    }

    response = requests.get(url, headers=headers)

    return response.json()

def get_character_location(vars):
    url = "https://esi.evetech.net/characters/2124597207/location"

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": vars["compatibility_date"],
        "X-Tenant": "",
        "If-Modified-Since": "",
        "Accept": "application/json",
        "Authorization": vars["auth_token"]
    }

    response = requests.get(url, headers=headers)

    return response.json()

def set_autopilot_waypoint(destination, vars, add_to_beginning="false", clear_other_waypoints="false"):
    url = "https://esi.evetech.net/ui/autopilot/waypoint"

    querystring = {"add_to_beginning":add_to_beginning,"clear_other_waypoints":clear_other_waypoints, "destination_id":destination}

    headers = {
        "Accept-Language": "",
        "If-None-Match": "",
        "X-Compatibility-Date": vars["compatibility_date"],
        "X-Tenant": "",
        "If-Modified-Since": "",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": vars["auth_token"]
    }

    response = requests.post(url, headers=headers, params=querystring)