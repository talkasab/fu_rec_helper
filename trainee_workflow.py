import streamlit as st

st.header("Working with Trainees", divider=True)

"""
Because the Follow-up Recommendations tool is to be used only at final signing 
time, trainees do not directly activate the tool. Nevertheless, trainees have an
important role to play in the process. It is important for trainees to create
reports that contain well-crafted recommendations. When the recommendations are
well-formed, at final signing, the attending can activate the tool, which will 
present the recommendations in the correctly-filled in dialog. The attending
then clicks/says "Accept", and the tool will send the recommendation to Epic
for management.
"""

st.subheader("Trainees: Creating Recommendations")

"""
When creating recommendations, trainees should follow these guidelines:

- The recommendable should be readibly identifiable to the final signer reviewing
  the report.
- All of the elements of the recommendation should be present and clear:
  - The modality and body part, along with the laterality, if applicable.
  - The date range, including both start end dates
  - The finding/reason for the recommendation
  - If needed, the code for specifying a specialized protocol

To assist in creating well-formed recommendations, trainees can use the "Macro
Recommendation" tool, which inserts a template recommendation into the report:
"""

st.image("images/macro_recommendation.png", caption="Macro Recommendation Tool")

"""
After inserting the template, the trainee fills in the fields:
"""

st.image(
    "images/macro_recommendation_filled.png", caption="Filled-in Macro Recommendation"
)

st.subheader("Final Signer: Formalizing Recommendations")

"""
**When opening the report to review/edit**, the final signer can activate the 
Follow-up Recommendations tool in the usual ways ("Launch Follow-up 
Recommendations", toolbar button, "Tools" menu item, Shift-F7). They then confirm 
that all the fields are filled in correctly, make sure the right finding is
associated with the recommendation, and click "Accept" for each appropriate 
recommendation.
"""

col1, col2 = st.columns([3, 1])

with col1:
    """
  **When reviewing reports in the signing list**, the final signer can activate
  the Follow-up Recommendations tool by clicking the toolbar button. They then
  confirm that all the fields are filled in correctly, make sure the right finding
  is associated with the recommendation, and click "Accept" for each appropriate
  recommendation.
  """

    st.image("images/from_signing_list.png", caption="Activating from Signing List")

with col2:
    st.page_link(
        "vid_signing_list.py",
        label="Signing List Usage",
        icon=":material/movie:",
    )
