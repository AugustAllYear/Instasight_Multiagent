#!/bin/bash
# Script to create GitHub Issues for each task in Instasight

set -e

echo "Creating GitHub Issues for Instasight tasks..."

# Define tasks as: "Title|Body|Label"
tasks=(
  "Fix Google ADK imports|Update agent imports to match official ADK API (e.g., from google.adk.agents import Agent).|bug"
  "Reimplement agent data flow|Create core data functions in each agent module and use them directly in orchestrator; ensure dataframes pass correctly between agents.|enhancement"
  "Add error handling to API calls and file I/O|Wrap Meta API calls, CSV reading, and file writing in try-except blocks with logging.|bug"
  "Create missing directories dynamically|Ensure 'exports/' directory exists before writing CSV/Tableau files; handle creation at runtime.|enhancement"
  "Validate environment variables|Check META_TOKEN, PAGE_ID before use; raise clear errors if missing.|bug"
  "Add logging throughout pipeline|Use consistent logging (info, warning, error) in ingestion, normalization, analysis, export steps.|enhancement"
  "Populate config.yaml|Add meaningful defaults to configs/config.yaml (paths, API env names, forecasting window).|enhancement"
  "Create config loader|Implement configs/config_loader.py to read YAML and merge with environment variables.|enhancement"
  "Add pyyaml to requirements.txt|Include pyyaml for YAML parsing.|chore"
  "Use config values in tools|Replace hardcoded paths and parameters with values from config.|enhancement"
  "Handle missing columns in analytics|In tools/analytics.py, ensure 'saves' column exists; default to 0.|bug"
  "Handle small data in forecasting|If fewer than 7 rows, fallback to mean instead of rolling average.|bug"
  "Create export directory in exporters|In tools/exporters.py, create export directory before writing files.|bug"
  "Add timeout and retry to Meta API|In tools/meta_api.py, add request timeout and basic retry logic.|enhancement"
  "Write unit tests for tools|Add tests/test_normalize.py, test_analytics.py, test_forecasting.py using pytest.|test"
  "Write integration test for full pipeline|Test the entire pipeline with a mock CSV file.|test"
  "Add GitHub Actions CI|Create .github/workflows/ci.yml to run tests on push.|ci"
  "Update README|Add corrected setup, environment variables, config usage, and logging.|docs"
  "Add Dockerfile improvements|Update Dockerfile to copy config and set up logging.|build"
)

for task in "${tasks[@]}"; do
  IFS='|' read -r title body label <<< "$task"
  echo "Creating issue: $title"
  # Create issue with label
  gh issue create --title "$title" --body "$body" --label "$label"
  # Small delay to avoid rate limits
  sleep 1
done

echo "All issues created."