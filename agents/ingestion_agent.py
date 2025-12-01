from google.generativeai.agents import Agent

ingestion_agent = Agent(
    name="instagram_ingestion_agent",
    instructions="Load Instagram data from upload or Meta API.",
    tools=[load_csv_tool, meta_api_tool],
    memory=InMemorySessionService(),
)