import streamlit as st

st.header("Training Checklist", divider=True)

"""
Please review each of the linked items below to ensure you are prepared to use the
Follow-up Recommendations tool effectively and avoid the pitfalls that can lead to
unactionable recommendations being sent to Epic, requiring manual intervention to
correct.

- Basic Usage (with video)
- Multiple Recommendations (with video)
- Trainee Workflow (with video)
- Review tip sheet
"""

pitfalls = """
### Pitfalls to Avoid

- Use the tool **only** at final sign time
- All fields must be filled in
- Time range (different start/end dates) are required
- Be aware of multiple recommendations
- All recommendations must be Accepted or Declined to send to Epic
- Do **NOT** press the "Flag for Review" button
"""
st.warning(icon=":material/warning:", body=pitfalls)
