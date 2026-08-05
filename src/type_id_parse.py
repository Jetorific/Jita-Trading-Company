import csv

with open("~/Jita-Trading-Company/src/data/eve_item_type_ID.txt","r") as f:
    result = f.readlines()

list_of_lines = []

for line in result:
    line = line.strip()
    components_of_line = line.split()
    list_of_lines.append(components_of_line)

for line in list_of_lines:
    if len(line) > 2:
        for num in range(2,len(line)):
            line[1] += " " + line[num]


with open("data/eve_type_id.csv", "w") as target_file:
    writer = csv.writer(target_file)
    writer.writerow(['typeID','typeName'])
    for num in range(1,len(list_of_lines)):
        writer.writerow([list_of_lines[num][0],list_of_lines[num][1]])




    



