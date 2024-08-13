import json
from tiktok_parser import filename

"""
Loads a JSON file as a Python dictionary.
"""
def load_json(file):
    f = open(file, encoding="utf8")

    data = json.load(f)
    f.close()

    return data

def parse_json():
    data = load_json(filename)
    pass

