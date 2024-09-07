import streamlit as st

st.header("Basic Usage: How to Use the Follow-up Tool", divider=True)

"""
This video shows an an example of using the tool to recommend a follow-up exam.

Note that while the video shows use of the "Macro: Recommendation" macro, to insert
standard language, this is not required. The tool will work with any clear language
that includes the required elements.
"""

col1, col2 = st.columns([3, 1])
with col1:
    """
  Also note that the video shows launching the tool using "Launch Follow-up 
  Recommendations" voice command. It is also possible to launch the tool by clicking
  the 🚩 (flag) or "Follow-up" button in the toolbar, choosing "Follow-up Recommendations"
  from the Tools menu, or pressing **Shift + F7**.
  """

col2.page_link(
    "vid_add_toolbar.py", label="How to add toolbar button", icon=":material/movie:"
)

"""
> **Key Points:**
> - The recommendation should include all the required elements
> - The start and end dates must be different, and the end date must be later than the start  
    (range as broad as possible, usually at least 1 month)
> - Use the tool at final sign time
> - Do not use the "Flag for Review" button
"""

st.video("videos/StraightforwardRecommendation2.mp4")
