from pathlib import Path

import streamlit as st

from constants import BASE_PAGE_TITLE


@st.cache_data
def get_file_content_as_bytes(path: str) -> bytes:
    # Make sure the file exists and is readable
    if not Path(path).is_file():
        raise FileNotFoundError(f"File not found: {path}")
    bytes = open(path, "rb").read()
    return bytes


# See https://discuss.streamlit.io/t/where-to-set-page-width-when-set-into-non-widescreeen-mode/959/15
def set_style(*, width: int, font_size_rem: float = 1.0):
    assert width >= 500 and width <= 1200, "Width must ≥500 and ≤ 1200."
    assert (
        font_size_rem >= 0.8 and font_size_rem <= 2.0
    ), "Font size must ≥1.0 and ≤ 2.0."
    st.html(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: {width}px;
    }}

    #stDecoration {{ visibility: hidden; }}

    p, ol, ul, dl {{
        font-size: {font_size_rem}rem !important;
    }}
    
    .st-emotion-cache-1sno8jx li {{
        font-size: {font_size_rem}rem !important;
    }}

    code{{
        color: #092090;
        background-color: #e0e0f0;
        font-size: 1.1rem;
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
    page_title=BASE_PAGE_TITLE,
    page_icon="images/favicon.png",
    # initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": ABOUT_TEXT,
    },
)
set_style(width=1000, font_size_rem=1.25)

st.logo("images/csr_action_name_horiz.png", icon_image="images/favicon.png")
st.image("images/csr_action_big_logo_horiz.png")

about = st.Page("about.py", title="About", default=True)
training = st.Page("training.py", title="Training Checklist")
basic_usage = st.Page("basic_usage.py", title="Basic Workflow")
multiple_recs = st.Page("multiple_recs.py", title="Multiple Recommendations")
field_guide = st.Page("field_guide.py", title="Dialog Fields")
mr_pelvis = st.Page("mr_pelvis.py", title="MR Pelvis")
covered_recs = st.Page("covered_recs.py", title="Covered Recommendations")
trainee_workflow = st.Page("trainee_workflow.py", title="Trainee Workflow")
dashboard = st.Page("dashboard.py", title="Recommendation Dashboard")
addending = st.Page("addending.py", title="Correcting Recommendations")
tip_sheet_faq = st.Page("tip_sheet_faq.py", title="Tip Sheet & FAQ")

vid_basic = st.Page("vid_basic.py", title="Basic Recommendation")
vid_multiple = st.Page("vid_multiple.py", title="Multiple Recommendations")
vid_report_code = st.Page("vid_report_code.py", title="Report Codes")
vid_consult = st.Page("vid_recommend_consult.py", title="Consult Recommendation")
vid_add_toolbar = st.Page("vid_add_toolbar.py", title="Add Toolbar Button")
vid_signing_list = st.Page("vid_signing_list.py", title="Signing List")

what_happens = st.Page("what_happens.py", title="Tool Simulator")
recommendables = st.Page("recommendables.py", title="How To + Recommendables")

app = st.navigation(
    {
        "About": [
            about,
            training,
            basic_usage,
            multiple_recs,
            field_guide,
            covered_recs,
            trainee_workflow,
            dashboard,
            addending,
            tip_sheet_faq,
            mr_pelvis,
        ],
        "Videos": [
            vid_basic,
            vid_multiple,
            vid_report_code,
            vid_consult,
            vid_add_toolbar,
            vid_signing_list,
        ],
        "Tools": [what_happens, recommendables],
    }
)

app.run()
