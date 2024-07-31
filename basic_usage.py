import streamlit as st

st.header("Basic Usage: How to Use the Follow-up Tool", divider=True)

col1, col2 = st.columns([4, 1])
col1.markdown("### 1. Dictate the recommendation in your report")


@st.dialog("Video", width="large")
def video_dialog(file_path: str):
    st.video(file_path, autoplay=True)


if col2.button("Show Video"):
    video_dialog("videos/StraightforwardRecommendation2.mp4")

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
  - Start and end days
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
- If the "Findings" drop-down does not contain an appropriate description of the reason
  for the recommendation, uncheck all the boxes and dictate the reason for recommendation
  in the text field below.
""")

col2.markdown("""
**Ways to Launch the Recommendations Tool**
- Dictate **Launch Follow-up Recommendations**
- Click the "Follow-up" button in the toolbar
- Choose "Follow-up Recommendations" from the Tools menu
- Press **Shift + F7**
""")

st.markdown("""### 3. Click/Say "Accept" to complete the recommendation
- After closing the Follow-up Recommendation tool, final sign your report
""")

st.subheader("Key Points", divider=True)
st.markdown("""
- Use the tool at final sign time
- Make sure to fill in all the required fields
""")
