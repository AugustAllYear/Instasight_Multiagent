import requests
import pandas as pd
import os

def load_from_meta_api(page_id=None):
    token = os.environ.get("META_TOKEN")

    url = f"https://graph.facebook.com/v19.0/{page_id}/media"
    params = {
        "fields": "timestamp,like_count,comments_count,media_type,impressions,reach,saved",
        "access_token": token
    }
    r = requests.get(url, params=params).json()
    data = r.get("data", [])
    return pd.DataFrame(data)
