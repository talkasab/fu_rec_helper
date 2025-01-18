import streamlit as st

st.header("⭐ New Trainee Workflow", divider=True)

"""
Beginning February 4, 2024, residents and fellows will have access to the Follow-up
Recommendations tool in PowerScribe and will be able to create structured recommendations
which are sent to Epic. This page provides an overview of the workflow for trainees and
attendings when trainees create recommendations in reports.
"""

st.info(
    """Trainees and attendings are strongly encouraged to discuss how trainees are
        expected to use the tool before trainees launch the tool for the first time.""",
    icon=":material/handshake:",
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Trainees")

    """
- Make sure you discuss if/how you’re going to use the tool with your attending.
- Because it is complex to alter or remove recommendations, we recommend that trainees 
  NOT use the tool until they’ve confirmed with the final-reading attending that they 
  will be making the recommendation (and what the parameters of that recommendation 
  will be).
- We recommend that you actually use the tool after discussing with your attending as 
  the final step in your work on the report before sending for attending final signature. 
- The steps for using the tool are as outlined in the basic workflow description and videos.
    """

    st.page_link("basic_usage.py", label="Basic Usage", icon=":material/link:")
    st.page_link("vid_basic.py", label="Video", icon=":material/movie:")
    st.page_link("what_happens.py", label="Tool Simulator", icon=":material/link:")
    st.page_link(
        "multiple_recs.py", label="Multiple Recommendations", icon=":material/link:"
    )
    st.page_link("vid_multiple.py", label="Video", icon=":material/movie:")

    """
#### Main tips

- **Make sure to include all required elements**: This is best done by making the 
  recommendation in the report text in one complete, concise statement, such as:

  > Recommend follow-up chest CT in 3-6 months for the 7mm right upper lobe nodule.

- **Provide distinct start/end times** for the follow-up exam to offcur (i.e., a time
  range), noting:
  - If the follow-up needs to happen within less than 14 days, you should use the CSR
    Acknowledge (PCAF) tool instead of the CSR Action (Follow-up Recommendations) tool.
  - Always provide the broadest possible time range that is clinically appropriate to
    allow for flexibility in scheduling.
- **Check the findings**: Uncheck NLP-recognized options in the findings field that are 
  not relevant to the recommendation.
- **Never click “Flag for Review”**
- **Be aware of multiple recommendations** accept or decline each detected recommendation 
  and then use the “OK” button to finalize
- **Insert the _1 Action_ macro** at the bottom of your report. This text is the only 
  indication to the attending that you have already formalized the recommendation with
  the tool.
    """

    st.info("“Macro ‘1 Action’”", icon=":material/voice_selection:")

    """

##### Output

> Follow-up recommendations were communicated and documented using a closed loop
> communication system. 
    """

with col2:
    st.subheader("Attendings")

    """
- Make sure to discuss with trainees you work with how you expect them to use the tool.
- We recommend that trainees only use the tool **after** confirming with you and **immediately
  before** releasing the report for attending final sign (e.g., when prelim-signing).
- No recommendation information is sent to Epic until the attending final-signs
  the report
- Especially remind trainees to include the “1 Action” macro—but only once they have used 
  the tool (e.g., last step)
- If you see the macro (“Follow-up recommendations were communicated and documented...”) in
  a trainee report, you know the discussed recommendation has been made using the tool.
- If you need to change the recommendation the trainee made, the steps are:
  - Make the change to the recommendation text in the report
  - Activate the Follow-up Recommendations tool
  - Go through **all** of the recommendations in the tool, accepting/declining each one.
  - If needed, add any undetected recommendations from scratch.
  - Press “OK” to finalize
- When making changes to recommendations that have been previously made using the tool,
  (before final signing) you **must** review and re-accept/decline each recommendation 
  and press the “OK” button to finalize all changes.
"""
