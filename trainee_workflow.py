import streamlit as st

st.header("Working with Trainees", divider=True)

"""
Because the Follow-up Recommendations tool is to be used only at final signing 
time, trainees do not directly activate the tool. Nevertheless, trainees have an
important role to play. It is important for trainees to create reports that 
contain well-formed recommendations in the report. When they do so, at final 
signing, the attending can activate the tool, which presents the dialog fields
correctly and completed filled with the recommendation information. The attending
clicks/says "Accept", and the tool sends the recommendation to Epic.
"""

st.subheader("Trainees: Creating Recommendations")

"""
When creating recommendations, trainees should follow these guidelines:

- The recommendable should be readibly identifiable to the final signer reviewing
  the report.
- All of the elements of the recommendation should be present and clear:
  - The modality and body part, along with the laterality, if applicable.
  - The date range, including both start date and end date (greater than the start)
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


with col2:
    st.page_link(
        "vid_signing_list.py",
        label="Signing List Usage",
        icon=":material/movie:",
    )

st.image("images/from_signing_list.png", caption="Activating from Signing List")
