from esi_helpers import *
import requests
import csv

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id


esi = ESIHelper({"player_id": read_player_id(), "compatibility_date":"2026-08-18"})


market_data = esi.get_market_prices()


for item in market_data:
    item_info = esi.get_item_info(item["type_id"])
    item_info.pop("dogma_attributes",None)
    for key in item_info.keys():
        item[key] = item_info[key]

csv_file_list = [[market_data[0].keys()]]

for item in market_data:
    holderlist = []
    for key in item.keys():
        holderlist.append(item[key])
    csv_file_list.append(holderlist)


with open("data/complete_market_data.csv", "w") as target_csv:
    writer = csv.writer(target_csv)
    writer.writerows(csv_file_list)

#note to later self, good luck getting this nightmare spaghetti code to actually output anything useful, ESI has 0 guidelines on how often you should be calling the get_item_info
#also I came up with most of this logic at 3 in the morning, so it might probably work?