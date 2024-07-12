import streamlit as st

st.header("How to Use the Follow-up Tool")

col1, col2 = st.columns([2, 3])
col1.markdown(
    """
#### Dictate the Recommendation in Your Report
- The recommendation should include:
  - Modality of the recommended exam 
  - Body part to be imaged
  - Laterality (if relevant)
  - Start and end days
  - Finding to be evaluated / Reason for recommendation
- Example: "Recommend chest CT in 6 to 8 months for
pulmonary nodule."
- We have created a macro (**Macro: Recommendation**)
to make it easier to include the required information.
- EMR Follow-up tool works better with clearer language,
as given by the macro.
"""
)

col2.image("images/how_to_1.png", use_column_width=True)
col2.image("images/how_to_2.png", use_column_width=True)

col1, col2 = st.columns([3, 2])
