import requests

class ESIHelper:
    vars = None

    def __init__(self, vars):
        self.vars = vars

    def names_to_ids(self, names):
        url = "https://esi.evetech.net/universe/ids"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        if isinstance(names, str):
            names = [names]
        else:
            names = list(names)
        response = requests.post(url, json=names, headers=headers)

        return response.json()

    def get_wallet_balance(self):
        url = f"https://esi.evetech.net/characters/{self.vars['player_id']}/wallet"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json",
            "Authorization": self.vars["auth_token"]
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def get_character_location(self):
        url = "https://esi.evetech.net/characters/2124597207/location"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json",
            "Authorization": self.vars["auth_token"]
        }

        response = requests.get(url, headers=headers)

        return response.json()

    def set_autopilot_waypoint(self, destination, add_to_beginning="false", clear_other_waypoints="false"):
        url = "https://esi.evetech.net/ui/autopilot/waypoint"

        querystring = {"add_to_beginning":add_to_beginning,"clear_other_waypoints":clear_other_waypoints, "destination_id":destination}

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": self.vars["auth_token"]
        }

        response = requests.post(url, headers=headers, params=querystring)