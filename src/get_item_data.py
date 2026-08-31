from esi_helpers import *
import requests
import csv
import time


def read_player_id() -> str:
    with open("player_id", "r") as f:
        player_id = f.read()
    return player_id


esi = ESIHelper({"player_id": read_player_id(), "compatibility_date":"2026-08-18"})


market_data = esi.get_market_prices()

initial_market_data_index = 0

with open("src/data/complete_typeid_list.csv","r") as file:
    itemlist = list(csv.reader(file))
itemlist.pop(0)

useful_info = ["type_id","name","volume","packaged_volume","mass","market_group_id","icon_id","group_id","capacity"]

with open("src/data/complete_item_info_list.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(useful_info)
    useful_info.pop(0)
    for item in itemlist:
        attributewriter = []
        attributedict = {}
        attributewriter.append(item[0])
        attributedict = esi.get_item_info(item[0])
        if type(attributedict) != dict:
            time.sleep(30)
            attributedict = esi.get_item_info(item[0])
        for item_attribute in useful_info:
           attributewriter.append(attributedict.get(item_attribute,None))
        writer.writerow(attributewriter)
           
        
       

