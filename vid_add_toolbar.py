import streamlit as st

st.header("Adding the Follow-up Tool to the Toolbar", divider=True)
col1, col2 = st.columns([2, 3])
with col1:
    """
    Some users will not see the 🚩 (flag) or "Follow-up" toolbar item in PowerScribe. 
    To add the toolbar button, choose the dropdown that adds/removes buttons from the 
    toolbar and find the “Follow-up Recommendations” icon with the flag (see image and
    video). You should only have to do this once. 
    """
with col2:
    st.image("images/add_toolbar_button.png")

st.video("videos/AddFollowupToolbarButton.mp4")
