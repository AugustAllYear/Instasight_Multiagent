import pandas as pd

def engagement_analysis(data):
    data["eng_rate"] = (data["likes"] + data["comments"] + data["saves"]) / data["reach"].replace(0, 1)
    return {
        "average_engagement_rate": data["eng_rate"].mean(),
        "top_posts": data.nlargest(5, "eng_rate").to_dict(orient="records")
    }

def posting_patterns(data):
    data["hour"] = data["post_timestamp"].dt.hour
    data["weekday"] = data["post_timestamp"].dt.day_name()
    return {
        "best_hour": int(data.groupby("hour")["eng_rate"].mean().idxmax()),
        "best_weekday": data.groupby("weekday")["eng_rate"].mean().idxmax()
    }

def content_clustering(data):
    return {
        "type_summary": data.groupby("content_type")["eng_rate"].mean().to_dict()
    }
