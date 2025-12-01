import streamlit as st
from orchestrator.run_pipeline import run_full_pipeline

st.title("IMIA — Multi-Agent Instagram Intelligence")

file = st.file_uploader("Upload Meta Export (CSV)", type=["csv"])

if file:
    st.write("Running pipeline...")
    analysis, bi_export = run_full_pipeline(file)

    st.subheader("Insights")
    st.write(analysis)

    st.download_button(
        "Download PowerBI Export",
        open(bi_export["result"], "rb"),
        file_name="imia_bi_export.csv"
    )
