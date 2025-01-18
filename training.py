import streamlit as st

st.header("Training Checklist", divider=True)

col1, col2 = st.columns(2)

with col1:
    """
Please review each of the linked items below to ensure you are prepared to use the
Follow-up Recommendations tool effectively and avoid the pitfalls that can lead to
unactionable recommendations being sent to Epic, requiring manual intervention to
correct.
  """

pitfalls = """
### Pitfalls to Avoid

- Use the tool **only** as the last step in working with the report
  - Trainees: Before prelim signing or releasing for attending review
  - Attendings: Before final sign 
- All fields must be filled in
- Time range (different start/end dates) are required (range as broad as possible, usually at least 1 month)
- Be aware of multiple recommendations
- All recommendations must be Accepted or Declined to send to Epic
- Do **NOT** press the "Flag for Review" button
"""
col2.warning(icon=":material/warning:", body=pitfalls)

st.divider()

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("""#### Basic Usage

Learn the basics of how to use the Follow-up Recommendations tool in PowerScribe to
create actionable recommendations and send them to Epic. 
                
Make sure to understand how to fill in all the required fields.

Consider practicing with the tool simulator to see what would be recommended with
different inputs.
                """)

with col2:
    st.page_link("basic_usage.py", label="Basic Usage", icon=":material/link:")
    st.page_link("vid_basic.py", label="Video", icon=":material/movie:")
    st.page_link("what_happens.py", label="Tool Simulator", icon=":material/link:")

st.divider()

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("""#### Multiple Recommendations

Learn how to handle multiple recommendations in a single report, and to be aware that
the tool may find more recommendations than expected. E.g., if the report text says
"CT Abdomen Pelvis", the tool will recognize both "CT Abdomen" and "CT Pelvis"; each
recommendation must be accepted or declined.
                """)

with col2:
    st.page_link(
        "multiple_recs.py", label="Multiple Recommendations", icon=":material/link:"
    )
    st.page_link("vid_multiple.py", label="Video", icon=":material/movie:")

st.divider()
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("""#### Trainee Workflow

Understand how trainees will use the tool and how attendings should guide them in
its use.
                """)

with col2:
    st.page_link(
        "trainee_workflow.py", label="Trainee Workflow", icon=":material/link:"
    )

st.divider()
st.markdown("""#### Pitfalls

Watch the video below showing the problems that arise when we dictate "in 6 months"
or "recommend CT Abdomen/Pelvis" in our reports—and how to avoid them.
            """)

st.video(
    "videos/pitfalls.mp4", autoplay=False, muted=False, subtitles="videos/pitfalls.vtt"
)
