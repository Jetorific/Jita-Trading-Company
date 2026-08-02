from esi_helpers import *

def read_player_id():
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id

def read_auth_token():
    with open("auth.tok", "r") as f:
        auth_tok = f.read()
    return auth_tok

def main():
    esi = ESIHelper({
        "auth_token" : read_auth_token(),
        "player_id" : read_player_id(),
        "compatibility_date" : "2026-07-21"
    })

    system_id = esi.names_to_ids("Sirppala")['systems'][0]['id']
    print(esi.set_autopilot_waypoint(system_id, clear_other_waypoints="true"))

if __name__ == "__main__":
    main()