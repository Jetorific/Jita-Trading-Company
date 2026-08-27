from esi_helpers import *
import requests
import csv

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id


esi = ESIHelper({"player_id": read_player_id(), "compatibility_date":"2026-08-18"})


market_data = esi.get_market_prices()

initial_market_data_index = 0

with open("src/data/complete_typeid_list.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["type_id"])
    for item in market_data:
        writer.writerow([item["type_id"]])
