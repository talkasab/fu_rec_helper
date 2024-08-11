import streamlit as st

col1, col2 = st.columns([3, 1])
with col1:
    st.header("Managing Multiple Recommendations", divider=True)

with col2:
    st.page_link(
        "vid_multiple.py",
        label="Making Multiple  \nRecommendations",
        icon=":material/movie:",
    )

col1, col2 = st.columns([3, 3])
with col1:
    """
When the Follow-up Recommendations tool is launched, it will attempt to detect 
recommendations in your report and display them in the tool. If the tool detects
multiple recommendations, it will display the first one and allow you to page through
them.
    """

    st.warning(
        """
The tool may detect multiple recommendations in your report, some of which may be
unintended (e.g., when saying "CT Abdomen/Pelvis", getting separate recommendations
for "CT Abdomen" and "CT Pelvis"). If you see that multiple recommendations have 
been detected, make sure to review each one.
              """,
        icon=":material/warning:",
    )

with col2:
    st.info(
        """
#### Key Points
- The tool may detect multiple recommendations in your report
- Review each recommendation and associate the appropriate finding(s)
- Click "Accept" for each appropriate recommendation (and "Decline" otherwise)
- Click "OK" to finalize the recommendations (**closing the tool without 
  clicking "OK" will not send the recommendations**)
            """,
        icon=":material/key:",
    )


st.image("images/multiple_recs_interface.png")

"""
For each recommendation, associate the appropriate finding(s) with the recommendation,
including adding additional free text as needed. If the finding is appropriate to send
to Epic, click "Accept". If the recommendation is not appropriate, click "Decline".

Once all recommendations have been reviewed, click (or dictate) "OK" to finalize the 
recommendations. 
"""

st.warning(
    """
**If you do not click "OK" when complete, the accepted recommendations will not be sent!**
Clicking "Cancel" will close the tool without sending any recommendations, even those for 
which you have clicked "Accept".
    """,
    icon=":material/warning:",
)
