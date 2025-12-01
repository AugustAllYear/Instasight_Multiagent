from agents.ingestion_agent import run_ingestion
from agents.normalization_agent import run_normalization
from agents.imia_agent import run_imia
from agents.export_agent import run_export

def run_full_pipeline(file):
    step1 = run_ingestion(file)
    step2 = run_normalization(step1)
    step3 = run_imia(step2)
    step4 = run_export(step3)
    return step3, step4
