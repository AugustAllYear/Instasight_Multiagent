from google.generativeai.agents import Agent
from tools.exporters import create_powerbi_csv, create_tableau_extract

export_agent = Agent(
    name="bi_export_agent",
    instructions="Create BI-ready datasets from the IMIA analysis output.",
    tools=[create_powerbi_csv, create_tableau_extract],
)
