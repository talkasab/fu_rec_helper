import streamlit as st


# See https://discuss.streamlit.io/t/where-to-set-page-width-when-set-into-non-widescreeen-mode/959/15
def set_style(*, width: int):
    assert width >= 500 and width <= 1200, "Width must ≥500 and ≤ 1200."
    st.html(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: {width}px;
    }}

    #stDecoration {{ visibility: hidden; }}

    code{{
        color: #092090;
        background-color: #e0e0f0;
        font-size: 0.9em;
    }}
</style>
    """
    )


ABOUT_TEXT = """
# CSR Action Guide
This is an app to help radiologists at MGB recommend follow-up imaging. 
It shows what exams are recommended based on the body part, modality, and laterality selected. 
It also shows how to recommend each exam.
"""

st.set_page_config(
    page_title="CSR Action Guide",
    page_icon="📖",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": ABOUT_TEXT,
    },
)
set_style(width=1000)

st.title("CSR Action Guide")

what_happens = st.Page("what_happens.py", title="What Happens When I...?", default=True)
how_to_recommend = st.Page("how_to_recommend.py", title="How Do I Recommend...?")
recommendables = st.Page("recommendables.py", title="Recommendable Exams")

app = st.navigation([what_happens, how_to_recommend, recommendables])

app.run()
