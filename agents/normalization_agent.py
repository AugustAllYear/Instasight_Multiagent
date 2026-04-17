from google.adk import Agent
from tools.normalize_instagram_csv import normalize_instagram_csv
import logging

logger = logging.getLogger(__name__)

def normalize_data(raw_data):
    return normalize_instagram_csv(raw_data)

NORMALIZATION_INSTRUCTION = """
You are a normalization agent. Transform raw Instagram data into a clean, structured format.
Use the provided tool to perform normalization.
"""

normalization_agent = Agent(
    name="normalization_agent",
    instruction=NORMALIZATION_INSTRUCTION,
    tools=[normalize_instagram_csv],
)

def run_normalization(raw_data):
    return normalization_data(raw_data)