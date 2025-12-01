from google.generativeai.agents import Agent
from tools.exporters import create_powerbi_csv, create_tableau_extract

export_agent = Agent(
    name="bi_export_agent",
    instructions=open("configs/agent_instructions/exporter.md").read(),
    tools=[generate_powerbi_csv, generate_tableau_extract]
)

def run_export(analysis_output):
    return export_agent.run({"analysis": analysis_output})