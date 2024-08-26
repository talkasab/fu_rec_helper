import streamlit as st

st.header("Follow-up Recommendations Tool Fields", divider=True, anchor=False)


"""
The Follow-up Recommendations tool can be somewhat complex to manage at first.
This guide will help you understand the fields and how to use them to create
valid recommendations.
"""

col1, col2 = st.columns(2)
with col1:
    st.error(
        """
**Do NOT use the "Flag for Review" button!** It will prevent your recommendation
from being formatted correctly to send to Epic.
        """,
        icon=":material/error:",
    )

    st.warning(
        """
If you generate a recommendation with incomplete information, you will be contacted
by the Safety Net team, who will ask you to create an addendum for your report to 
use the tool to create a correctly-formed recommendation.
        """,
        icon=":material/warning:",
    )

with col2:
    st.info(
        """
## Key Points

- Must specify start end end dates, and end date must be different and greater
  than the start date.
- Must specify modality and body region
- Must specify laterality if relevant
- Must select appropriate findings and/or use free text
        """,
        icon=":material/key:",
    )

st.subheader("Start and End Days")

col1, col2 = st.columns([5, 2])
with col1:
    """
- The start and end days are used to generate the expected and expire date in
  the generated order in Epic.
- This must be a **range**, otherwise you are requesting that the exam be 
  performed **exactly** on the start date.
- The **start date** should be the earliest date for which an order for the exam
  meeting the criteria would be appropriate (e.g., if you are recommening a 6-
  month follow-up, if an exam in 5.5 months would be OK, you might choose a
  start days of 165 days).
- The **end date** should be the date after which the recommended exam would be
  overdue, and the Safety Net team should reach out to the patient's care team
  to help them make the exam happen, if it is still indicated.
"""

with col2:
    st.image(
        "images/dates_to_epic.png",
        caption="How the start and end dates are used in the Epic BPA and then in the generated order.",
    )

st.subheader("Modality, Body Region, and Laterality")

col1, col2 = st.columns([3, 1])

with col1:
    """
- The Modality and Body region fields are used to determine the exam for which an
  order will be generated for the provider. A back-end mapping process turns these
  combinations into valid orders in Epic. E.g., "MRI" and "Stomach" will be mapped
  to a "MR Abdomen" order.
- Procedure modalities and non-radiology modalities can be used to recommend consults,
  non-radiology imaging (e.g, echocardiography), and procedures (e.g., biopsy or 
  endoscopy).
- Not all combinations of modality and body region map to a valid exam (e.g., 
  "Mammography" and "Head")—if you create an invalid combination, it will require 
  an addendum so you can re-create the recommendation using the tool. See the list
  of "Recommendables" to see the exams that can be recommended.
- Some exams require laterality to be specified; if laterality is not specified, the
  recommendation will be unactionable and require an addendum. If laterality is not
  relevant, it doesn't matter what value is selected.
- For exams that require laterality, only a small handful allow "Bilateral" as an
  option; see the list of recommendable to see which exams allow this.
- To determine how to recommend a specific exam, go to the "How to Recommend" tool
  and choose the exam you want to recommend. The tool will return the valid combinations
  of modality and body region for that exam, as well as a report code, if required.
- Different combinations of modality and body regeion can be tested using the "Tool
  Simulator" link, and entering appropriate values in the fields—this will show the
  order that would be generated in Epic, along with allowed report codes that can be
  applied.
"""

with col2:
    st.page_link(
        "recommendables.py", label="All Recommendables", icon=":material/link:"
    )
    st.page_link(
        "how_to_recommend.py",
        label="How to Recommend  \nSpecific Exam",
        icon=":material/link:",
    )
    st.page_link("what_happens.py", label="Dialog Simulator", icon=":material/link:")


st.subheader("Reason for Recommendation: Findings and Free Text")

col1, col2 = st.columns(2)
with col1:
    """
- The NLP tool will detect numerous possible reasons for your exam and place them in the 
  "Finding" dropdown; all will be selected (and included with the recommendation in Epic)
  by default.
- Uncheck the detected findings to prevent inappropriate/duplicative ones from being sent 
  to Epic.
- If none of the detected findings are appropriate, or if additional information is needed,
  use the free-text field to enter a custom finding/reason for the recommendation.
    """

with col2:
    st.image(
        "images/findings_field.png",
        caption="The findings and free text fields in the dialog.",
    )
