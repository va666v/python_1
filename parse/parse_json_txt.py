import json

with open("sample_json.json", 'r') as fl:
        json_ = json.load(fl)

with open('new_txt.txt', "w") as file:
    json_ = str(json_)
    txt_ = file.write(json_)


