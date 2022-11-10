import json
import yaml


with open('sample_yaml.yml', 'r') as file:
    yaml_ = yaml.safe_load(file)

with open("new_json.json", 'a') as fl:
    json.dump(yaml_, fl)

