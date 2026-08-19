import requests
import eve_oauth
import json

class ESIHelper:
    REGION_INFORMATION_FILE = "src/data/universe/region_information.json"
    REGION_LIST_FILE = "src/data/universe/region_list.json"

    def __init__(self, vars):
        self.vars = vars
        self.tokens = eve_oauth.run_oauth_flow()

    ### API CALL FUNCTIONS ###

    # Get ids for each name in a list
    def names_to_ids(self, names: str | list[str]) -> dict:
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
        response.raise_for_status()
        return response.json()

    # Get names and categories for each id in a list
    def id_info(self, ids: int | str | list[int | str]) -> dict:
        url = "https://esi.evetech.net/universe/names"

        if isinstance(ids, str) or isinstance(ids, int):
            ids = [ids]
        else:
            ids = list(ids)
        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url, json=ids, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get a list of all regions
    def get_regions(self) -> list:
        url = "https://esi.evetech.net/universe/regions"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info about a region
    def get_region_info(self, region_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/regions/{region_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get a list of all constellations
    def get_constellations(self) -> list:
        url = "https://esi.evetech.net/universe/constellations"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info about a constellation
    def get_constellation_info(self, constellation_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/constellations/{constellation_id}"

        headers = {
            "Accept-Language": "",  
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info about a stargate
    def get_stargate_info(self, stargate_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/stargates/{stargate_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info about a system
    def get_solar_system_info(self, system_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/systems/{system_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars['compatibility_date'],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info about a station
    def get_station_info(self, station_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/stations/{station_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars['compatibility_date'],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get info of a given item's type_id
    def get_item_info(self, type_id: int | str) -> dict:
        url = f"https://esi.evetech.net/universe/types/{type_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

        
    # Get balance of current player
    def get_wallet_balance(self) -> dict:
        url = f"https://esi.evetech.net/characters/{self.vars['player_id']}/wallet"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.tokens['access_token']}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Set autopilot waypoint to destination
    def set_autopilot_waypoint(self, destination: int | str, add_to_beginning="false", clear_other_waypoints="false") -> dict:
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
            "Authorization": f"Bearer {self.tokens['access_token']}"
        }

        response = requests.post(url, headers=headers, params=querystring)
        response.raise_for_status()

    # Get location of current player, either region, system, or station
    def get_current_location(self) -> dict:
        url = f"https://esi.evetech.net/characters/{self.vars['player_id']}/location"

        headers = {
            "Accept-Language": "en",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.tokens['access_token']}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get market prices of various type_ids including adjusted and average price
    def get_market_prices(self) -> dict:
        url = "https://esi.evetech.net/markets/prices"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get all orders in the given region
    def get_orders_in_region(self, region_id: int | str, order_type="all", page=None, type_id=None) -> dict:
        url = f"https://esi.evetech.net/markets/{region_id}/orders"

        querystring = {"order_type":order_type}
        if page: querystring["page"] = page
        if type_id: querystring["type_id"] = type_id

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()

    # Get a list of orders in the given structure
    def get_orders_in_structure(self, structure_id: int | str) -> list:
        url = f"https://esi.evetech.net/markets/structures/{structure_id}"

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars[""],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.tokens['access_token']}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    # Get a list of type_ids that have open orders in the given region
    def get_relevant_type_ids(self, region_id: int | str, page=None) -> list:
        url = f"https://esi.evetech.net/markets/{region_id}/types"

        querystring = {}
        if page: querystring["page"] = page

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()

    # Get a list of historical data on a type_id in the given region
    def get_historic_market_stats(self, region_id: int | str, type_id: int | str) -> list:
        url = f"https://esi.evetech.net/markets/{region_id}/history"

        querystring = {"type_id": type_id}

        headers = {
            "Accept-Language": "",
            "If-None-Match": "",
            "X-Compatibility-Date": self.vars["compatibility_date"],
            "X-Tenant": "",
            "If-Modified-Since": "",
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()


    ### HELPER FUNCTIONS ###

    # Find the region a given system is part of
    def get_region_from_system(self, system_id: int | str) -> int:
        with open(self.REGION_INFORMATION_FILE, "r"):
            system_info = self.get_solar_system_info(system_id)
            constellation = system_info["constellation_id"]

            # Basic iterative approach for now
            with open(self.REGION_LIST_FILE, "r") as f:
                region_list = json.load(f)

            with open(self.REGION_INFORMATION_FILE, "r") as f:
                region_information = json.load(f)

            for region_id in region_list:
                if constellation in region_information[f"{region_id}"]["constellations"]:
                    return region_id