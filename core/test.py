import json

with open('../data/data.json') as data_file:
    data = json.load(data_file)

print(data)