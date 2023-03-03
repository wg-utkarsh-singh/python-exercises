import json

with open("company1.json", "r+") as f:
    d = json.loads(f.read())
    d["employees"].append({"firstName": "Albert", "lastName": "Bert"})
    f.seek(0)
    json.dump(d, f, indent=2, sort_keys=True)
    f.truncate()
