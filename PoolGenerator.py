#Victor Stolle PoolGenerator.py

'''
PoolGenerator.py will take in a csv file, and create a dictionary that will consist of:

mapname : htmlcode


'''

csv = open("swiss.csv", "r")

mappool = {}

for line in csv:
    split = line.split(",")
    html = ("<tr>\n<td>\n" + split[4] + '</td>\n<td>\n<a href="' + split[3] + '">' + split[1] + "</a>\n</td>\n<td>\n" + split[0] + "</td>\n<td>" + split[2] + "</td>\n<td>" + split[5] + "</td>\n<td>" + split[6] + "</td>\n</tr>\n")
    mappool[split[1]] = html

csv.close()

print(len(mappool.keys()))  


