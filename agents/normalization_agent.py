from google.generativeai.agents import Agent
from tools.normalizer import normalize_instagram_csv

normalization_agent = Agent(
    name="normalization_agent",
    instructions="Convert raw Meta export to normalized IMIA format.",
    tools=[normalize_instagram_csv],
)