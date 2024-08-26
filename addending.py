import streamlit as st

st.header("Correcting a Non-Actionable Recommendation", divider=True, anchor=False)

"""
We’d like to thank you for placing the follow-up recommendation for this exam as part
of the MGB CSR-Action program to help ensure timely performance of clinically-necessary 
follow up recommendations.  

Actionable recommendations in CSR-Action require imaging 
modality, body part, time range (earliest and latest timeframe you deem appropriate for 
your recommendation) and the rationale for follow up. 

Because the recommendation you created using the Follow-up Recommendations tool did 
not meet these requirements, **we ask that you create a new actionable recommendation** 
associated with your report.
"""

st.subheader("Steps to Correct your Recommendation")

col1, col2 = st.columns([6, 6])
with col1:
    """
1. Open the report for addending. Insert language to the effect of:  
   _"This addendum is to clarify a follow-up recommendation associated with
   the original report."_
2. Re-dictate a clarified recommendation into the addendum (you will not be able
   to modify the original report).
3. Use the Follow-up Recommendation tool to create a new recommendation meeting the requirements
   (see right).
4. "Accept" the recommendation in the dialog, and "Decline" all other recommendations.
5. Sign the addendum
6. Reply to the notification email so that the MGB Radiology Safety Net team can confirm 
   the new recommendation is actionable and can close the old recommendation.
   """

with col2:
    st.page_link(
        "basic_usage.py", label="How to Recommend", icon=":material/arrow_forward:"
    )
    st.image("images/about_1.png", use_column_width=True)
    """
#### Actionable Recommendation Requirements 

   - Specify a time frame with **different** start and end dates
   - Specify the modality and body region (± laterality)
   - Provide a rationale for follow-up ("Findings" or free text)
   - **Do not** click the "Flag for Review" button
   - **Accept** your corrected recommendation and **Decline** all others
"""

"""
Please let us know if you have any questions.
 
Thank you,  
_MGB Radiology Safety Net, MGB Radiology Quality Safety_
"""
