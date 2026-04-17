import streamlit as st
from orchestrator.run_pipeline import run_full_pipeline
from tools.logging_utils import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

st.title("IMIA — Multi-Agent Instagram Intelligence")

file = st.file_uploader("Upload Meta Export (CSV)", type=["csv"])

if file:
    with st.spinner("Running pipeline..."):
        try:
            analysis, exports = run_full_pipeline(file)
            st.subheader("Insights")
            st.write(analysis)
            # Provide download button
            with open(exports["powerbi"]["result"], "rb") as f:
                st.download_button(
                    "Download PowerBI Export",
                    f,
                    file_name="imia_bi_export.csv"
                )
        except Exception as e:
            st.error(f"Pipeline failed: {e}")
            logger.exception("Pipeline error in Streamlit")