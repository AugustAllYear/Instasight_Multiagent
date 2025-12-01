from google.generativeai.agents import Agent
from tools.analytics import (
    engagement_analysis,
    posting_time_analysis,
    forecasting_model,
)

imia_agent = Agent(
    name="imia_agent",
    instructions="""You are the Instagram Metrics Intelligence Agent (IMIA). 
Analyze normalized datasets and produce insights, predictions, and strategy.""",
    tools=[engagement_analysis, posting_time_analysis, forecasting_model],
    memory=MemoryBank(),   
    parallel_tool_calls=True,
)