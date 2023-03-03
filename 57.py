import json
from pprint import pprint

with open("company1.json") as file:
    d = json.loads(file.read())
    pprint(d)
