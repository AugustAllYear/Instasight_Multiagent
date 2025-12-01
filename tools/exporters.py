import pandas as pd

def generate_powerbi_csv(analysis):
    df = pd.DataFrame(analysis["top_posts"])
    df.to_csv("exports/imia_bi_export.csv", index=False)
    return "exports/imia_bi_export.csv"

def generate_tableau_extract(analysis):
    # Placeholder for Tableau .hyper file
    return "exports/tableau_extract.hyper"
