import pandas as pd

def generate_powerbi_csv(analysis):
    """Write top posts to CSV for PowerBI."""
    df = pd.DataFrame(analysis.get("top_posts", []))
    df.to_csv("exports/imia_bi_export.csv", index=False)
    return {"result": "exports/imia_bi_export.csv"}

def generate_tableau_extract(analysis):
    """Placeholder for Tableau .hyper export."""
    # Actual implementation would use e.g., tableauhyperapi
    return {"result": "exports/tableau_extract.hyper"}