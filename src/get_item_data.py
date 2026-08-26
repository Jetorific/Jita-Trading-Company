from esi_helpers import *
import requests
import csv
import pdb

def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id


esi = ESIHelper({"player_id": read_player_id(), "compatibility_date":"2026-08-18"})


market_data = esi.get_market_prices()

initial_market_data_index = 0

with open("src/data/complete_market_data.csv", "a") as target_csv:
    writer = csv.writer(target_csv)
    writer.writerow(list(market_data[0].keys()))
    for num in range(initial_market_data_index,len(market_data)):
        try:
            item_info = esi.get_item_info(market_data[num]["type_id"])
            item_info.pop("dogma_attributes",None)
            item_info_list = []
            for key in item_info.keys():
                item_info_list.append(item_info[key])
            writer.writerow(item_info_list)
            initial_market_data_index +=1
        except KeyboardInterrupt:
            writer.writerow([initial_market_data_index])
            exit

# No actual changes were really made this rev, but main thing I need to figure out in the coming days is a nice way to run part of this list and then stop after that.
# FOLLOW UP TO THE ABOVE, I'm going to have to completely re-write all of this, it's not parsing the data in the way I expected it to, but the file writing does seem to be working somehow. Also the keyboard interrupts are borked af.