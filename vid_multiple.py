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

st.header("Offering Alternatives", divider=True)

"""
A common situation for radiologists is recommending either of two exams for following
up a lesion. 

In this case, the radiologist can dictate both recommendations in the report
and then use the tool to select the appropriate recommendation. The tool will likely 
detect both recommendations; the radiologist should choose the one they favor, and then
decline the other. The provider will then have the option to easily order the favored
exam (accepted recommendation), but can still decide to order the other exam and have
it be tracked.

The below shows a radiologist recommending either a CT or an MR in the report, and then
favoring the MR in the tool (by declining the CT).
"""

st.video("videos/RecommendCTorMR.mp4")
