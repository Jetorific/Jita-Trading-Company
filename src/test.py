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

    print(esi.get_wallet_balance())
    # system_id = esi.names_to_ids("Jita")['systems'][0]['id']
    # esi.set_autopilot_waypoint(system_id, clear_other_waypoints="true")
    # alt_tab()
    # gui_autopilot()
    # alt_tab()

if __name__ == "__main__":
    main()