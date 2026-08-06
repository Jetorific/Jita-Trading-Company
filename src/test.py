from esi_helpers import *
# from gui_tools import *

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

def main() -> None:
    esi = ESIHelper({
        "player_id" : read_player_id(),
        "compatibility_date" : "2026-07-21"
    })

    location = esi.get_current_location()
    region_id = esi.get_region_from_system(location["solar_system_id"])

    print(location)
    print(region_id)
    print(esi.get_region_info(region_id))

if __name__ == "__main__":
    main()