import streamlit as st

st.header("About the CSR Action Program", divider=True)

"""
The **Clinically Significant Results: Action** program facilitates efficient ordering, 
scheduling, and tracking to completion of radiologist recommendations for additional 
imaging or follow-up care, when appropriate.
"""

st.image("images/emr_fu_dialog.png", use_column_width="never")

"""
When a clinician agrees with a radiologist recommendation, they can order the exam (or
have someone order it for them) and schedule the exam via their clinic scheduling 
mechanisms. 
"""

st.image("images/provider_popup.png", use_column_width="auto")

"""
The exam is also automatically tracked by safety net team  to ensure the patient 
receives the exam during the timeframe recommended.
"""

st.image("images/order_followup.png", use_column_width="auto")

"""
This program can extend cover both imaging and non-imaging follow-up recommendations, 
including recommendations for biopsies and consultation, ensuring patients receive
appropriate follow-up care.
"""
