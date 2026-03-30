import pandas as pd

def normalize_instagram_csv(raw_data):
    """
    Normalize raw Instagram data (CSV or DataFrame) into a standard schema.
    Handles missing columns gracefully.
    """
    df_raw = raw_data if isinstance(raw_data, pd.DataFrame) else pd.read_csv(raw_data)

    column_map = {
        "likes": ["like_count", "likes"],
        "comments": ["comment_count", "comments"],
        "saves": ["saved", "save_count"],
        "impressions": ["impressions"],
        "reach": ["reach"],
        "followers": ["followers", "follower_count"],
        "post_timestamp": ["timestamp", "published", "created_time"],
        "content_type": ["media_type", "content_type"],
    }

    df = pd.DataFrame()

    for target, potentials in column_map.items():
        for pot in potentials:
            if pot in df_raw.columns:
                df[target] = df_raw[pot]
                break
        if target not in df:
            # Set default values for missing columns
            if target == "post_timestamp":
                df[target] = pd.NaT
            else:
                df[target] = 0

    # Standardize timestamp
    df["post_timestamp"] = pd.to_datetime(df["post_timestamp"], errors="coerce")
    df["days_since_post"] = (pd.Timestamp.now() - df["post_timestamp"]).dt.total_seconds() / 86400

    # Normalize content type
    df["content_type"] = df["content_type"].astype(str).str.lower()

    return df