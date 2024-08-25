import json
import pandas as pd
from tiktok_ad_scraper import filename

"""
Loads a JSON file as a Python dictionary.
"""
def load_json(file):
    # Opening the file containing the JSON data
    f = open(file, encoding="utf8")
    # Loading the data
    data = json.load(f)
    f.close()

    return data

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

"""
Stores JSON data into a Pandas DataFrame.
"""
def extract_json():
    data = load_json("tiktok-sample-data.json")
    #pd.set_option('display.max_columns', None)

    # Extract the 'materials' list from the JSON data
    materials = data['data']['materials']

    # Flatten each object in the materials list
    flattened_materials = [flatten_dict(item) for item in materials]

    # Create a DataFrame from the flattened list
    df = pd.DataFrame(flattened_materials)

    # Cleans the DataFrame so the data is more usable
    df = clean_data(df)

    """
    ads = data['data']['materials']

    for ad in ads:
        ad_title = ad['ad_title']
        brand_name = ad['brand_name']
        cost = ad['cost']
        ctr = ad['ctr']
        ad_id = ad['ad_id']
        ad_industry = ad['industry_key'].replace("label_", "")
        is_search = ad['is_search']
        ad_likes = ad['like']
        ad_objective = ad['objective_key'].replace("campaign_objective_", "")
        ad_duration = ad['video_info']['duration']
        ad_video_link = ad['video_info']['video_url']['720p']
    """

"""
Cleans the given DataFrame to remove unnecessary data and reformat desired data into a more usable format.
"""
def clean_data(df):
    # adjust campiagn objective column
    # adjust industry key column - is there a way to convert this into the name and not just the ID?
    # remove extra columns
    pass

extract_json()