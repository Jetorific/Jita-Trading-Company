from esi_helpers import *
import json

# Parses json return and writes to file
def save_json_file(data: dict, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

MARKET_PRICES_FILE = "src/data/market_data.json"

# Saves market prices to a file
def save_market_prices(esi: ESIHelper):
    save_json_file(esi.get_market_prices(), MARKET_PRICES_FILE)
    print(f"Saved market prices to {MARKET_PRICES_FILE}")