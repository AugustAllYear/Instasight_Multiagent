from google.adk import Agent
from tools.exporters import generate_powerbi_csv, generate_tableau_extract

EXPORT_INSTRUCTION = """
You are a BI export agent. Convert analysis results into PowerBI CSV and Tableau Hyper extracts.
"""

export_agent = Agent(
    name="bi_export_agent",
    instruction=EXPORT_INSTRUCTION,
    tools=[generate_powerbi_csv, generate_tableau_extract],
)

def run_export(analysis_output):
    return export_agent.run(f"Export analysis: {analysis_output}")