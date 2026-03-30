from google.adk import Agent
from tools.analytics import (
    engagement_analysis,
    posting_patterns,
    content_clustering
)
from tools.forecasting import metrics_forecast

IMIA_INSTRUCTION = """
You are the IMIA analysis agent. Use the provided tools to analyse Instagram data:
- Compute engagement metrics and top posts.
- Find best posting times and days.
- Summarise performance by content type.
- Provide a forecast.
"""

imia_agent = Agent(
    name="imia_analysis_agent",
    instruction=IMIA_INSTRUCTION,
    tools=[engagement_analysis, posting_patterns, content_clustering, metrics_forecast],
    parallel_tool_calls=True,
)

def run_imia(normalized_data):
    return imia_agent.run(f"Analyse: {normalized_data}")