from google.generativeai.agents import Agent
from tools.meta_api import load_from_meta_api
from tools.utils import load_uploaded_csv
from google.generativeai.agents.sessions import InMemorySessionService

ingestion_agent = Agent(
    name="instagram_ingestion_agent",
    instructions=open("configs/agent_instructions/ingestion.md").read(),
    tools=[load_uploaded_csv, load_from_meta_api],
    memory=InMemorySessionService()
)

def run_ingestion(input_file):
    return ingestion_agent.run({"file": input_file})
