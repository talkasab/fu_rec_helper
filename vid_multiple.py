import streamlit as st

st.header("Multiple Recommendations", divider=True)

"""
This video shows an example of using the tool to recommend multiple follow-up exams
from a single report.

Note that while the first recommendation uses "Macro: Recommendation" to insert the
standard language, the second recommendation is dictated using natural language (which
still includes the required elements).

Also see the arrows at the bottom of the tool being used to move between the different
recommendations.

Finally, note the use of the "Findings" dropdown to make sure that the correct reason(s)
are associated with the each recommendation—that is, the pulmonary nodule finding is
associated with the Chest CT recommendation while the humeral lesion is associated with
the MRI of the humerus recommendation. 
"""

st.video("videos/MultipleRecommendations2.mp4")
