from client import TS_CLIENT, SCHEMA
import json,pprint

print("-" * 10, "START TEST QUERY")


try:
    with open("../data/search.json", "r") as f:
        search_parameters = json.load(f)

except:
    with open("./search.json", "r") as f:
        search_parameters = json.load(f)

print("-" * 10, "Search parameters")
pprint.pprint(search_parameters)

print("-" * 10, "Query output")

res = TS_CLIENT.collections[SCHEMA['name']].documents.search(search_parameters)

pprint.pprint(res)