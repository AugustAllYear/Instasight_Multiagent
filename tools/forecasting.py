def metrics_forecast(data):
    # Simple forecasting placeholder
    # KPIs tbd by user
    avg_growth = data["eng_rate"].rolling(7).mean().iloc[-1]
    return {"predicted_eng_rate": float(avg_growth)}
