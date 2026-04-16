import pandas as pd
import logging
from configs.config_loader import load_config

logger = logging.getLogger(__name__)

def metrics_forecast(data):
    config = load_config()
    window = config.get('forecasting', {}).get('window_days', 7)
    if "eng_rate" not in data:
        data["eng_rate"] = (data["likes"] + data["comments"] + data["saves"]) / data["reach"].replace(0, 1)
    if len(data) < window:
        logger.warning(f"Only {len(data)} rows, using mean instead of rolling forecast")
        predicted = data["eng_rate"].mean()
    else:
        predicted = data["eng_rate"].rolling(window).mean().iloc[-1]
    return {"predicted_eng_rate": float(predicted)}