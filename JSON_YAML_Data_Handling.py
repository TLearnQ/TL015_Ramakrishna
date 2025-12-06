import yaml
import json
with open("nested.json", "r") as f:
    data = json.load(f)
    print(data)
for keys, values in data.items():
    a = 1
    with open(f"{a}.json", "w") as l:
        json.dump(data, l)
        a += 1