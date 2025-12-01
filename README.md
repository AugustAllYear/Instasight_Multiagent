# Instasight: Multi Intelligence Agent

A start to finish data science multi-agent that delivers Instagram user insights extending beyond Meta Business, customizable to user-defined KPIs.

IMIA is a modular multi-agent system that ingests Instagram data via API or CSV, applies LLM-powered analytics and forecasting, and outputs BI-ready datasets for PowerBI, Tableau, or interactive dashboards.

IMIA Instasight (Multi Intelegence Agent) is a **multi-agent system** built with **Google Agent Developer Kit (ADK)** and Python. It ingests Instagram data, normalizes it, performs advanced analytics, and produces BI-ready exports suitable for **PowerBI** or **Tableau**. The platform supports both **manual CSV ingestion** and automated **Meta API ingestion**.

IMIA leverages a **modular architecture** with LLM-powered agents for analytics, normalization, and prediction, along with parallel and sequential execution for maximum efficiency.  

---

## Features

- **Multi-Agent Architecture**: Ingestion, normalization, analysis, and BI export agents.
- **Data Normalization**: Converts raw Meta Business Suite exports into a structured schema with datetime-aware metrics.
- **Insights & Forecasting**: LLM-powered engagement insights, trend analysis, and predictive modeling.
- **BI Export**: Generates PowerBI (.csv/.xlsx) and Tableau (.hyper) ready datasets.
- **Flexible Deployment**: Run locally via Streamlit or deploy in Google Cloud using Vertex AI and ADK.

---

## Project Structure

```text
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

### 🛠 Technologies & Roles

| Technology / Tool                  | Role in IMIA                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| **Python**                         | Core language for agents, tools, and orchestration                          |
| **LLM / OpenAI API**               | Generates insights, trend analysis, and forecasting                        |
| **Google ADK / Vertex AI**         | Orchestrates multi-agent workflows, supports long-running tasks, deployment|
| **Streamlit**                      | Interactive web UI for data upload, visualization, and exploration         |
| **Meta Graph API**                 | Optional ingestion of Instagram Business metrics                           |
| **Pandas / NumPy**                 | Data processing, normalization, and numeric computations                   |
| **PowerBI & Tableau**              | Targets for BI-ready exports (.csv, .hyper)                                 |
| **venv & .env**                     | Python environment management and secure configuration                     |
| **Custom Python Modules / Tools**  | CSV normalization, analytics, forecasting, API connectors, BI export       |
| **Sequential & Parallel Agents**   | Efficient execution of dependent or concurrent tasks                        |
| **Looping Agents**                 | Recurring tasks and batch processing                                        |
| **Sessions & Memory**              | Maintains state and historical metrics for intelligent decision-making     |
| **Context Engineering**            | Optimizes LLM context for meaningful insights on metrics                   |


---

## Project Structure

1. Clone the Repository: please see github user guides for information on how to clone the repo and launch it locally.


2. Set Up a Virtual Environment in the local clone of the repository by navigating to the Repo directory on your local device and entering the commands (one at a time)

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies
bash
Copy code
pip install -r requirements.txt


4. Configure Environment Variables

create .env file by entering the following commands in your terminal:
note: this may not work if the enviroment is activated then you will need to manually add them to the folder.

touch .env
Add the following:

Contents the .env Copy code:
GOOGLE_API_KEY=your-google-adk-api-key
GOOGLE_PROJECT_ID=your-gcp-project-id
GOOGLE_LOCATION=us-central1

META_TOKEN=your-meta-access-token       # Optional for API ingestion
PAGE_ID=your-instagram-page-id

GCS_BUCKET=imia-data-exports
ENABLE_API_INGESTION=True
📥 Data Ingestion Options
IMIA supports two ways to get Instagram data:

5. DATA input options
Option 1: Meta API (Automatic)
    1. Create a Facebook Developer App: https://developers.facebook.com

    2. Enable Instagram Graph API in the app.

    3. Connect your Instagram Business Account to your Facebook Page.

    4. Generate a Long-Lived Access Token (valid ~60 days) with these permissions:

nginx
Copy code
instagram_basic
instagram_manage_insights
instagram_manage_comments
pages_show_list
pages_read_engagement
    5. Add the token and page ID to your .env file:

env
Copy code
META_TOKEN=EAAG...
PAGE_ID=your-page-id
Enable API ingestion in .env:

env
Copy code
ENABLE_API_INGESTION=True
Run the Streamlit app. IMIA will automatically fetch new posts, insights, and engagement metrics.

Option 2: Manual CSV Export (Offline)
Go to Meta Business Suite → Insights → Export Data.

Select your Instagram Page and the desired date range.

Download the CSV (Excel or CSV format).

Open Streamlit and upload the CSV file.

IMIA agents will automatically normalize the CSV, convert post dates to datetime objects, and prepare the data for analysis.

✅ This option works without a Meta Access Token, but requires manual data export.

🖥 Run Streamlit UI
bash
Copy code
streamlit run streamlit_app.py
Access your local dashboard:

arduino
Copy code
http://localhost:8501
Upload a CSV or use API ingestion. The agents will process the data, normalize it, and provide BI-ready exports in exports/.

📊 Exports
exports/imia_bi_export.csv → PowerBI/Tableau CSV

exports/tableau_extract.hyper → Tableau Hyper Extract

Both include:

Date dimensions

Content metrics (likes, comments, shares, saves)

Engagement rates

LLM-predicted performance metrics

⚙️ Architecture Overview
IMIA uses:

LLM-powered agents for analysis

Sequential & parallel agent execution

Custom tools for CSV normalization and forecasting

Google ADK / Vertex AI for orchestration and deployment

Streamlit for a user-friendly interface
