import requests
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

def load_from_meta_api(page_id=None):
    token = os.environ.get("META_TOKEN")
    if not token:
        raise ValueError("META_TOKEN environment variable not set")
    if not page_id:
        page_id = os.environ.get("PAGE_ID")
        if not page_id:
            raise ValueError("PAGE_ID not provided and not set in environment")
    url = f"https://graph.facebook.com/v19.0/{page_id}/media"
    params = {
        "fields": "timestamp,like_count,comments_count,media_type,impressions,reach,saved",
        "access_token": token
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json().get("data", [])
        logger.info(f"Fetched {len(data)} posts from Meta API")
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Meta API error: {e}")
        raise