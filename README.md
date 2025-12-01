# Instasight_Multiagent
A start to finish data science multi-agent that delivers Instagram user insights extending beyond Meta Business, customizable to user-defined KPIs.


## Project Structure

imia-system/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── normalization_agent.py
│   ├── imia_agent.py
│   ├── export_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── normalize_instagram_csv.py
│   ├── analytics.py
│   ├── forecasting.py
│   ├── exporters.py
│   ├── meta_api.py
│   └── utils.py
│
├── orchestrator/
│   └── run_pipeline.py
│
├── streamlit_app.py
│
├── configs/
│   ├── config.yaml
│   └── agent_instructions/
│       ├── ingestion.md
│       ├── normalization.md
│       ├── imia_brain.md
│       └── exporter.md
│
├── exports/
│   ├── imia_bi_export.csv
│   └── tableau_extract.hyper
│
├── requirements.txt
├── README.md
└── .env
