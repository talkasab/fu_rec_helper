from pathlib import Path

import streamlit as st


@st.cache_data
def get_file_content_as_bytes(path: str) -> bytes:
    # Make sure the file exists and is readable
    if not Path(path).is_file():
        raise FileNotFoundError(f"File not found: {path}")
    bytes = open(path, "rb").read()
    return bytes


st.video("videos/tip_sheet.mp4", autoplay=True, loop=True, muted=True)

st.header("About the CSR Action Program", divider=True)

"""
The **Clinically Significant Results: Action** program facilitates efficient ordering, 
scheduling, and tracking to completion of radiologist recommendations for additional 
imaging or follow-up care, when appropriate.

Within PowerScribe, radiologists dictate their recommendations and then activate the
integrated Follow-up Recommendations tool to create a structured recommendation:
"""

st.image("images/about_1.png", use_column_width="auto")

"""
When the radiologist signs their report, the structured recommendation is sent to Epic
with their report. The patient's care team is alerted to the recommendation as they
interact with the patient's record:
"""

st.image("images/provider_popup.png", use_column_width="auto")

"""
From this alert, the provider can choose how to proceed with the recommendation. If
the recommendation is not appropriate, they can decline it or reroute it to a 
different provider. If the recommendation is accepted, the provider can go to 
directly ordering the recommended exam, with the details from the recommendation
pre-populated in the order:
"""

st.image("images/order_followup.png", use_column_width="auto")

"""
The exam is also automatically tracked by safety net team  to ensure the patient 
receives the exam during the timeframe recommended.

This program can extend cover both imaging and non-imaging follow-up recommendations, 
including recommendations for biopsies and consultation, ensuring patients receive
appropriate follow-up care.
"""
