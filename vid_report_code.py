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
