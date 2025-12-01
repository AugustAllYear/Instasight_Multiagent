from google.generativeai.agents import Agent
from tools.analytics import (
    engagement_analysis,
    posting_patterns,
    content_clustering
)
from tools.forecasting import metrics_forecast
from google.generativeai.agents.memory import MemoryBank

imia_agent = Agent(
    name="imia_analysis_agent",
    instructions=open("configs/agent_instructions/imia_brain.md").read(),
    tools=[engagement_analysis, posting_patterns, content_clustering, metrics_forecast],
    parallel_tool_calls=True,
    memory=MemoryBank()
)

def run_imia(normalized_data):
    return imia_agent.run({"data": normalized_data})
