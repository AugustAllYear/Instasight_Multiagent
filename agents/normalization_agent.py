from google.adk import Agent
from tools.normalize_instagram_csv import normalize_instagram_csv

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
    return normalization_agent.run(f"Normalize: {raw_data}")