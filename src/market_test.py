from esi_helpers import *
import json

# need esi_helpers to get market data
# need json to save market data to file

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

# Parses json return and writes to file, probably need to do more post processing later
def save_market_prices(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

MARKET_PRICES_FILE = "src/data/market_data.json"

def main() -> None:
    esi = ESIHelper({
        "player_id" : read_player_id(),
        "compatibility_date" : "2026-07-21"
    })

    save_market_prices(esi.get_market_prices(), MARKET_PRICES_FILE)
    print(f"Saved market prices to {MARKET_PRICES_FILE}")

if __name__ == "__main__":
    main()