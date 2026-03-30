# Correct import for Google ADK (adjust if different)
from google.adk import Agent
from tools.meta_api import load_from_meta_api
from tools.utils import load_uploaded_csv

# Provide a basic instruction – replace with your actual content
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
    # ADK agents typically use `run` with a message string
    return ingestion_agent.run(f"Load data from: {input_file}")