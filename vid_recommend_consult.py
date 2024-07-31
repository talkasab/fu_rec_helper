import streamlit as st

st.header("Recommending a Consult", divider=True)

"""
This video shows an an example of using the tool to recommend a consultation rather
than a follow-up imaging exam. In essence, the radiologist uses the tool to create a
recommendation with modality "Consult" and body part that indicates the location of
the finding that's prompting the consult. (The details of the service to be consulted
would be specified in the text of the report, or in the free-text field.)

Note that when recommending a consult, the tool will not automatically extract the
required fields, and the radiologist moves through the fields (using keyboard or
PowerMic buttons) and dictates or types the required information, including the 
reason for the consult in the free-text field below the (empty) "Findings" field.
"""

st.video("videos/ConsultRecommendation.mp4")
