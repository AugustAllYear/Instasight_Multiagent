# Correct import for Google ADK (adjust if different)
from google.adk import Agent
from tools.meta_api import load_from_meta_api
from tools.utils import load_uploaded_csv
import logging

def ingest_data(input_file):
    if hasattr9input_file, 'read'): 
        logger.info("Loading from uploaded CSV")
        return load_uploaded_csv(input_file)
    else:
        logger.info("Loading from Meta API")
        return load_from_meta_api()
        
INGESTION_INSTRUCTION = """
You are an ingestion agent. Load data from either a CSV file or Meta API.
Return the raw data as a pandas DataFrame.
"""

ingestion_agent = Agent(
    name="instagram_ingestion_agent",
    instruction=INGESTION_INSTRUCTION,
    tools=[load_uploaded_csv, load_from_meta_api],
)

def run_ingestion(input_file):
    # For ADK could use agent. but choosing core function direct in pipeline
    # return ingestion_agent.run(f"Load data from: {input_file}")
    return ingest_data(input_file)