import json
import yaml

with open("sample_json.json", 'r') as fl:
    json_ = json.load(fl)

with open('new_yaml.yml', 'a') as file:
    yaml.dump(json_, file)
