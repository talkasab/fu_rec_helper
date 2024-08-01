import streamlit as st

st.header("Formalizing Recommendations from the Signing Queue", divider=True)

"""
When recommendations are contained in the text of a report but not yet formalized
using the Follow-up Recommendations tool, the radiologists can activate the tool
from their signing queue without opening the exam to formalize the recommendation.
"""

col1, col2 = st.columns([3, 1])
with col1:
    """
    This might be useful when working with trainees, who have used the "Macro:
    Recommendation" to insert a recommendation with all the required fields for 
    convenience at final-signing time.
    """

col2.page_link(
    "vid_add_toolbar.py", label="Add toolbar button", icon=":material/movie:"
)

st.video("videos/SigningList.mp4")
