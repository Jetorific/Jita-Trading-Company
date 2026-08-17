from esi_helpers import *
import json

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

# Parses json return and writes to file
def save_json_file(data: dict, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

MARKET_PRICES_FILE = "src/data/market_data.json"

# Saves market prices to a file
def save_market_prices(esi: ESIHelper):
    save_json_file(esi.get_market_prices(), MARKET_PRICES_FILE)
    print(f"Saved market prices to {MARKET_PRICES_FILE}")


esi = ESIHelper({"player_id": read_player_id(), "compatibility_date":"2026-07-21"})

save_market_prices(esi)
# alright, so, the JSON response for save_market_prices returns a list of dictionaries, with one dictionary per item listed in the market
# the dictionaries contain the following: {"adjusted_price":float,"average_price":float,"type_id":int}
# still no effing idea what adjusted price corresponds to though

market_data = esi.get_market_prices()

print(type(market_data))