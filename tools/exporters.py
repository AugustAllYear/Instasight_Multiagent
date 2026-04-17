import pandas as pd
import os
import logging
from configs.config_loader import load_config

logger = logging.getLogger(__name__)

def generate_powerbi_csv(analysis):
    config = load_config()
    export_dir = config['paths']['exports']
    os.makedirs(export_dir, exist_ok=True)
    filename = config['export']['powerbi_filename']
    filepath = os.path.join(export_dir, filename)
    df = pd.DataFrame(analysis.get("top_posts", []))
    try:
        df.to_csv(filepath, index=False)
        logger.info(f"Exported PowerBI CSV to {filepath}")
    except Exception as e:
        logger.error(f"Failed to export CSV: {e}")
        raise
    return {"result": filepath}

def generate_tableau_extract(analysis):
    config = load_config()
    export_dir = config['paths']['exports']
    os.makedirs(export_dir, exist_ok=True)
    filename = config['export']['tableau_filename']
    filepath = os.path.join(export_dir, filename)
    # Placeholder: in real implementation, create .hyper file
    logger.info(f"Tableau extract placeholder at {filepath}")
    return {"result": filepath}