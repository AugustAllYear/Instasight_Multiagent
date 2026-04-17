import pandas as pd
import logging

logger = logging.getLogger(__name__)

def _ensure_eng_rate(data):
    data = data.copy()
    if "eng_rate" not in data:
        # Ensure required columns exist
        for col in ["likes", "comments", "saves", "reach"]:
            if col not in data:
                data[col] = 0
        data["eng_rate"] = (data["likes"] + data["comments"] + data["saves"]) / data["reach"].replace(0, 1)
    return data

def engagement_analysis(data):
    data = _ensure_eng_rate(data)
    return {
        "average_engagement_rate": data["eng_rate"].mean(),
        "top_posts": data.nlargest(5, "eng_rate").to_dict(orient="records")
    }

def posting_patterns(data):
    data = _ensure_eng_rate(data)
    data["hour"] = data["post_timestamp"].dt.hour
    data["weekday"] = data["post_timestamp"].dt.day_name()
    return {
        "best_hour": int(data.groupby("hour")["eng_rate"].mean().idxmax()),
        "best_weekday": data.groupby("weekday")["eng_rate"].mean().idxmax()
    }

def content_clustering(data):
    data = _ensure_eng_rate(data)
    return {
        "type_summary": data.groupby("content_type")["eng_rate"].mean().to_dict()
    }