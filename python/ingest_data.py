import json
import typesense

from client import TS_CLIENT, SCHEMA

try:
    with open("../data/data.json", "r") as f:
        data = json.load(f)

except:
    with open("./data.json", "r") as f:
        data = json.load(f)

print("CREATING SCHEMA")
create_response = TS_CLIENT.collections.create(SCHEMA)

print(create_response)

print("Ingesting data")
for item in data:
    res = TS_CLIENT.collections[SCHEMA['name']].documents.create(item)
    print("Item import response:")
    print("\t", res)

retrieve_all_response = TS_CLIENT.collections[SCHEMA['name']].retrieve()
print("NUMBER OF DOCUMENTS IN COLLECTION:", retrieve_all_response['num_documents'])
