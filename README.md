# Instasight: Multi-Intelligence Agent for Instagram Insights

A multi‑agent system that ingests Instagram data (via CSV or Meta API), normalizes it, applies LLM‑powered analytics and forecasting, and outputs BI‑ready datasets for PowerBI and Tableau.

---

## Features
- Multi‑agent architecture (ingestion, normalization, analysis, export)
- Data normalization of Meta Business Suite exports into a standard schema
- LLM‑powered insights (engagement analysis, posting patterns, content clustering, forecasting)
- BI exports – CSV for PowerBI and Tableau Hyper extract (placeholder)
- Two ingestion modes – CSV upload (offline) or Meta API (automatic)
- Streamlit UI for easy interaction

---

## Tech Stack

| Component            | Technology                     |
|----------------------|--------------------------------|
| Core language        | Python                         |
| Multi‑agent framework| Google Agent Development Kit   |
| LLM integration      | Google Gemini (via ADK)        |
| Data processing      | pandas, numpy                  |
| UI                   | Streamlit                      |
| API ingestion        | Meta Graph API, requests       |
| BI exports           | CSV, Tableau Hyper (planned)   |

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
```

### Technologies & Roles

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

## Setup & Installation

1. **Clone the repository**
```bash
   git clone https://github.com/your-username/Instasight_Multiagent.git
   cd Instasight_Multiagent
```
   

2. **Create a virtual environment (Python 3.9+)**
```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
```
3. **Install dependencies**

```bash
   pip install -r requirements.txt
```
4. **Configure environment variables (create a ```.env``` file)**
```text
    GOOGLE_API_KEY=your-google-api-key
    GOOGLE_PROJECT_ID=your-gcp-project-id
    GOOGLE_LOCATION=us-central1
    META_TOKEN=your-meta-access-token   # optional for API ingestion
    PAGE_ID=your-instagram-page-id
    GCS_BUCKET=imia-data-exports
    ENABLE_API_INGESTION=True
```
5. Run Streamlit
```bash
    streamlit run streamlit_app.py
```
---

## Data Ingestion Options
IMIA supports two ways to get instagram data:

**Option 1: Meta API (Automatic)**
1. Create a [Facebook Developer App](https://developers.facebook.com/)

2. Enable Instagram Graph API in the app.

3. Connect your Instagram Business Account to your Facebook Page.

4. Generate a Long‑Lived Access Token (valid ~60 days) with these permissions:
```text
    instagram_basic
    instagram_manage_insights
    instagram_manage_comments
    pages_show_list
    pages_read_engagement
```
5. Add the token and page ID to your ```.env``` file:
```text
    META_TOKEN=EAAG...
    PAGE_ID=your-page-id
```
6. Set ```ENABLE_API_INGESTION= TRUE``` in ```.env```
7. Run the streamlit app. IMIA will automatically fetch new posts, insights and engagement metrics.

**Option 2: Manual CSV Export (Offline)**
1. Go to Meta Business Suite → Insights → Export Data.

2. Select your Instagram Page and the desired date range.

3. Download the CSV (Excel or CSV format).

4. Open Streamlit and upload the CSV file.

5. IMIA agents will normalize the CSV, convert post dates to datetime objects, and prepare the data for analysis.

*This option works without a Meta Access Token, but requires manual data export.*

## Agent Instructions
The agents are configured using markdown instruction files that define their roles and tools. These files are located in configs/agent_instructions/.
- ```ingestion.md``` – Instructs the ingestion agent to load data from CSV or Meta API using the provided tools.
- ```normalization.md``` – Guides the normalization agent to apply column mapping and datetime conversion.
- ```imia_brain.md``` – Directs the analysis agent to compute engagement metrics, posting patterns, content clusters, and forecasts.
- ```exporter.md``` – Instructs the export agent to generate PowerBI CSV and Tableau Hyper extracts.

Each file contains a clear description of the agent’s purpose and the tools it should use, enabling the LLM to orchestrate the workflow correctly.

## Exports
After processing, the following files are generated in the exports/ directory:

- ```imia_bi_export.csv``` – PowerBI‑ready CSV with top posts and engagement metrics.

- ```tableau_extract.hyper``` – Placeholder for a Tableau Hyper extract (implementation planned).

Both files include date dimensions, content metrics (likes, comments, shares, saves), engagement rates, and LLM‑predicted performance metrics.

## Architecture Overview
IMIA leverages:

- LLM‑powered agents for analysis, guided by detailed instructions.

- Sequential and parallel agent execution for efficiency.

- Custom Python tools for CSV normalization, analytics, forecasting, and BI exports.

- Google ADK / Vertex AI for orchestration and deployment.

- Streamlit for a user‑friendly interface.

## CI/CD and Future Work
**CI/CD intergration**

- Automated Testing: Use GitHub Actions to run unit tests (e.g., pytest for tools) and integration tests on every push.

- Containerization: Build a Docker image for the Streamlit app and push to a container registry.

- Continuous Deployment: Deploy the app to Google Cloud Run or a similar platform on merge to main.

- Scheduled Pipelines: Set up cron jobs (via GitHub Actions or Cloud Scheduler) to run the ingestion pipeline daily when API mode is enabled, refreshing data and exports.

- Data Version Control: Integrate DVC to track dataset changes and model outputs.

- Monitoring: Add logging and alerting (e.g., Sentry) to catch runtime errors.

**Future Enhancements**

- Advanced Forecasting: Replace the simple rolling average with Prophet, ARIMA, or LSTM models.

- Sentiment Analysis: Analyze comment sentiment using LLMs or NLP libraries.

- Content Clustering: Use embeddings to group posts by topic or visual style.

- Multi‑Platform Support: Extend agents to handle TikTok, LinkedIn, and other social media APIs.

- Custom KPIs: Allow users to define their own business metrics.

- Automated Reporting: Generate weekly reports sent via email or Slack.

- Deploy as Managed Agents: Use Vertex AI Agent Engine for scalable, long‑running tasks.

- Feedback Loop: Allow users to validate insights and improve prompt instructions.

**Expanded Use Cases**

The architecture behind Instasight is intentionally platform‑agnostic. The system is built around a flexible data ingestion layer (CSV or any REST API), a normalization pipeline, and an LLM‑powered analytics layer, making it adaptable to a wide range of data sources and domains.

Example applications:

- Multi‑platform social intelligence – Ingest data from TikTok, YouTube, Twitter/X, or LinkedIn via their APIs; normalize engagement metrics and generate unified dashboards.

- Competitor benchmarking – Monitor multiple competitor accounts across platforms to compare growth, engagement, and content strategy.

- Influencer evaluation – Score potential partners based on historical engagement rates, audience growth, and sentiment.

- Customer feedback analysis – Process support tickets, reviews, or survey responses to identify recurring themes and sentiment trends.

- Operational log analysis – Analyze internal system logs to detect anomalies, forecast workloads, or summarize incident patterns.

- E‑commerce review mining – Extract product insights from customer reviews to inform development and marketing decisions.

The system provides a reusable template for automating data collection, normalizing messy inputs, and surfacing actionable insights—whether the data comes from social media, business systems, or customer interactions.




## Contact

- **Author**: August Vollbrecht
- **GitHub**: [github.com/AugustAllYear](https://github.com/AugustAllYear)
- **LinkedIn**: [linkedin.com/in/august-vollbrecht](https://www.linkedin.com/in/august-vollbrecht)
- **Email**: augustvollbrecht@proton.me

For questions, feedback, or collaboration opportunities, feel free to reach out.

























