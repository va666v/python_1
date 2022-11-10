import yaml

with open('sample_yaml.yml', 'r') as file:
    yaml_ = yaml.safe_load(file)

with open('new_txt_yaml.txt', "w") as file:
    yaml_ = str(yaml_)
    txt_ = file.write(yaml_)
