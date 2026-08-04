import csv

with open("~/Jita-Trading-Company/src/eve_item_type_ID.txt","r") as f:
    result = f.readlines()

holderlist = []

for item in result:
    item = item.strip()
    newitem = item.split()
    holderlist.append(newitem)

for item in holderlist:
    if len(item) > 2:
        for num in range(2,len(item)):
            item[1] += " " + item[num]


with open("eve_type_id.csv", "w") as tarf:
    wr = csv.writer(tarf)
    wr.writerow(['typeID','typeName'])
    for num in range(1,len(holderlist)):
        wr.writerow([holderlist[num][0],holderlist[num][1]])




    



