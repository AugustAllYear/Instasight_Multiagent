from google.generativeai.agents import Agent
from tools.normalize_instagram_csv import normalize_instagram_csv

normalization_agent = Agent(
    name="normalization_agent",
    instructions=open("configs/agent_instructions/normalization.md").read(),
    tools=[normalize_instagram_csv],
)

def run_normalization(raw_data):
    return normalization_agent.run({"raw_data": raw_data})
