import typesense, json

TS_CLIENT = typesense.Client({
    'api_key':                    'test',
    'nodes':                      [{
        'host':     'test-typesense',
        'port':     '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
})

try:

    with open("../data/schema.json", "r") as f:
        SCHEMA = json.load(f)
except:

    with open("./schema.json", "r") as f:
        SCHEMA = json.load(f)