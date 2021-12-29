import json

import yaml


def load_config(config_path: str):
    with open(config_path, 'r') as f:
        if config_path.endswith("yml"):
            config = yaml.load(f, Loader=yaml.FullLoader)
        elif config_path.endswith("json"):
            config = json.load(f)
        else:
            raise ("Invalid format. Only yml, json")
    return config


def prettify(expression: str):
    pass
