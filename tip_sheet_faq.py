import streamlit as st


@st.cache_data
def faq_text():
    with open("faq.md", "r") as f:
        return f.read()


policy_tab, tip_sheet_tab = st.tabs(["Policy FAQ", "Tip Sheet"])

policy_tab.markdown(faq_text())

tip_sheet_tab.image("images/tip_sheet.png")
