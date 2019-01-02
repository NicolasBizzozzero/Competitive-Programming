import json
import csv
from pprint import pprint


PATH_FILE_JSON = "Liste-Wifi"
PATH_FILE_TSV = "Liste-Password"
PATH_FILE_OUTPUT = "output.csv"


id_hash = dict()
hash_clear = dict()
id_clear = dict()


with open(PATH_FILE_JSON) as file:
    for w in json.load(file):
        id_hash[w["ap"]] = w["hash"]
        id_clear[w["ap"]] = None


with open(PATH_FILE_TSV) as file:
    reader = csv.reader(file, delimiter=" ")

    for line in reader:
        hash_clear[line[0]] = line[1]

hash_test = dict()
for k, v in hash_clear.items():
    hash_test[k] = v.replace("urhs", "").replace(
        "tye", "").replace("lqx", "").replace("x", "")


print(hash_test)

# for (id, hash) in id_hash.items():
#     try:
#         id_clear[id] = hash_clear[hash]
#     except KeyError:
#         pass


# with open(PATH_FILE_OUTPUT, "w") as output:
#     writer = csv.writer(output, delimiter=";")

#     for (id, clear) in id_clear.items():
#         writer.writerow([id, clear])
