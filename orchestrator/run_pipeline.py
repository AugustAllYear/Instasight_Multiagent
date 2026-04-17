from agents.ingestion_agent import ingest_data
from agents.normalization_agent import normalize_data
from agents.imia_agent import analyze_data
from agents.export_agent import export_results
from tools.logging_utils import setup_logging

logger = setup_logging()

def run_full_pipeline(file):
    logger.info("Starting pipeline")
    try:
        raw = ingest_data(file)
        logger.info("Ingestion complete")
        normalized = normalize_data(raw)
        logger.info("Normalization complete")
        analysis = analyze_data(normalized)
        logger.info("Analysis complete")
        exports = export_results(analysis)
        logger.info("Export complete")
        return analysis, exports
    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        raise