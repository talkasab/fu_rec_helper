import streamlit as st

st.header("Report Codes: Recommend a Specialized Protocol", divider=True)

"""
This video shows an an example of using a report code to create a more specialized
version of a recommendation.
"""

col1, col2 = st.columns([3, 1])
col1.markdown("""
After specifying the recommendation in your report, you can use **Macro: Special**
to insert a picklist field in your report allowing you to select among commonly used
specialized protocols (e.g., "With Contrast", "Special Handling", "Arthrogram", etc.).
              
Choose the appropriate code or dictate the choice name to insert the code in your report,
which will look something like this: `{REC:CTChestILD}`.
              
Note that the **Macro: Recommendation** also inserts this field at the end of the 
recommendation language it inserts (blank by default).
              
After inserting the report code, launch the Follow-up Recommendations tool as normal.
""")

col2.image("images/report_code_pick_list.png")

st.video("videos/ReportCode2.mp4")

st.subheader("Less Common Report Codes", divider=True)

col1, col2 = st.columns([3, 1])
with col1:
    """
  The pick list in the **Macro: Special** macro includes commonly used report codes,
  but a much larger set of specialized protocols can be specified. The complete list
  of recommendable exams includes many exams that cannot be specified with modality/
  body part combinations but for which report codes are available.
  """

col2.page_link(
    "recommendables.py", label="All Recommendable Exams", icon=":material/table:"
)

"""
To find and insert less common report codes, a Clinical Guidance module named "CSR
Recommendables" is available that has all report codes, organized by division. 

To use the tool to insert a report code:
- Activate the tool:
  - By choosing it from the Clinical Guidance tab at the bottom of the PowerScribe window
  - By dictating "Guidance: CSR Recommendables." 
- Choose the desired report code from the appropriate dropdown
- Click "Insert" to bring the code into the tet of your report

The video below shows an example.
"""

st.video("videos/ClinicalGuidanceReportCode.mp4")

col1, col2 = st.columns([3, 1])
with col1:
    """
  It is also possible to insert a report code by copying and pasting it from this
  Guide site; just select the report code, including the curly braces (`{...}`), and
  paste it into your report, either near your recommendation or at the bottom.
  """

col2.page_link(
    "recommendables.py", label="Report Codes for Exams", icon=":material/menu_open:"
)
