import streamlit as st

st.header("Basic Usage: How to Use the Follow-up Tool", divider=True)

st.video("videos/tip_sheet.mp4", autoplay=True, loop=True, muted=True)

col1, col2 = st.columns([4, 1])
col1.markdown("### 1. Dictate the recommendation in your report")

col2.page_link("vid_basic.py", label="Show Video", icon=":material/movie:")

st.image("images/how_to_1.png", use_column_width="auto")
col1, col2 = st.columns(2)
col1.markdown(
    """
- The recommendation should include all the required elements
- Example: "Recommend chest CT in 6 to 8 months for
pulmonary nodule."
- We have created a macro (**Macro: Recommendation**)
to make it easier to include the required information.
- EMR Follow-up tool works better with clearer language,
as given by the macro.
"""
)
col2.markdown("""
#### Required Elements
  - Modality of the recommended exam 
  - Body part to be imaged
  - Laterality (if relevant)
  - **Distinct** start and end days
  - Finding to be evaluated / Reason for recommendation
""")

st.markdown("### 2. Before signing, launch and use the Follow-up Recommendations Tool")
st.image("images/how_to_2.png")
col1, col2 = st.columns(2)
col1.markdown("""
- **At final sign time**, launch the follow-up recommendations tool
- Use either the mouse or dictation commands to move between fields and fill them in
- Though the tool will allow you to create an incomplete recommendation, please **fill in
  all the fields** 
- Be sure to use **distinct** start and end days
- If the "Findings" drop-down does not contain an appropriate description of the reason
  for the recommendation, uncheck all the boxes and dictate the reason for recommendation
  in the text field below.
- Do **NOT** use the "Flag for Review" button; this will result in a mal-formed 
  recommendation and you will be contacted by the Radiology Safety Net team.
""")

col2.markdown("""
**Ways to Launch the Recommendations Tool**
- Dictate **Launch Follow-up Recommendations**
- Click the "Follow-up" button in the toolbar.
- Choose "Follow-up Recommendations" from the Tools menu
- Press **Shift + F7**
""")

col2.page_link(
    "vid_add_toolbar.py", label="How to add toolbar button", icon=":material/movie:"
)

st.markdown("""### 3. Click/Say "Accept" to complete the recommendation
- After closing the Follow-up Recommendation tool, final sign your report
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader(":material/key: Key Points", divider=True)
    st.markdown("""
  - Use the tool at final sign time
  - Make sure to fill in all the required fields
  - Make sure the end days is greater than the start day
  - Do **not** use the "Flag for Review" button
  """)

with col2:
    st.subheader(":material/label_important: Malformed Recommendations", divider=True)
    st.markdown("""
  Malformed recommendations might be:
  - Nonsensical/non-mapped modality/body part
  - Incomplete fields (especially start and end days)
  - Start and end days are the same or end day is before start day
  - Missing appropriate laterality 
  - "Flag for Review" button was pressed

  Such incomplete recommendations are routed to the Radiology Safety Net team, who 
  are likely to contact you for clarification. You may be required to generate 
  an addendum with a new, correctly-formed recommendation.
  """)
