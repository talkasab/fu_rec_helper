import streamlit as st

from constants import (
    ADDITIONAL_IMAGING,
    BODY_PART_OPTIONS,
    LATERALITY_UNSPECIFIED,
    MODALITY_OPTIONS,
    SPECIAL_RECOMMENDABLES,
)
from utils import (
    get_fallback_recommendable,
    get_recommendable,
    get_report_codes_for_recommendable,
    get_report_form_for_code,
    load_data,
)

mappings, report_codes, recommendables, modality_mappings = load_data()


field_keys = ["start_days", "end_days", "modality", "body_part", "laterality", "show"]


def set_state_from_query():
    query_params = st.query_params.to_dict()
    if "show" not in query_params:
        query_params["show"] = False  # type: ignore
    st.session_state.update(**query_params)


def set_query_from_state():
    query_params = {
        key: val
        for key in field_keys
        if key in st.session_state and (val := st.session_state[key])
    }
    st.query_params.from_dict(query_params)


if not hasattr(st.session_state, "submitted"):
    set_state_from_query()


st.header("What Happens When I...?")

"""
Select a time frame,  modality, body part, and (if needed) laterality to see what
recommendation would be sent to Epic for the provider to consider and possibly
order. **Remember to use distinct start and end days for the recommendation!**
"""


def set_submitted_state():
    set_query_from_state()
    st.session_state.submitted = True


with st.form(key="my_form"):
    col1, col2 = st.columns(2)
    start_days_str = col1.text_input("Start Days", key="start_days")
    end_days_str = col2.text_input("End Days", key="end_days")
    modality = st.selectbox("Modality", MODALITY_OPTIONS, key="modality")
    body_part = st.selectbox(
        "Body Region", BODY_PART_OPTIONS, format_func=lambda x: x, key="body_part"
    )
    laterality = st.selectbox(
        "Laterality",
        ["", "Left", "Right", "Bilateral", "Unspecified", "Unilateral"],
        key="laterality",
    )
    submit_button = st.form_submit_button(
        label="Show Recommendation", on_click=set_submitted_state
    )


def get_markdown_for_recommendable(recommendable: str, icon: str = "white_check_mark"):
    markdown = f"#### :{icon}: Recommendation: **{recommendable}**\n"
    if recommendable in SPECIAL_RECOMMENDABLES:
        markdown += "\n" + SPECIAL_RECOMMENDABLES[recommendable]
    return markdown


def get_markdown_for_report_codes(report_codes: list[tuple[str, str]]):
    markdown = """### :mag: Report Codes\n\n"""

    markdown += """Report codes allow the radiologist to specify a recommended exam 
    more precisely than a modality/body part combination, such that the generated order
    is for the correct exam/protocol or procedure."""

    markdown += "\n\n"

    markdown += "Code | Recommended Exam\n" + "--- | ---\n"
    for code, description in report_codes:
        # markdown += f"- **{description}**: `{get_report_form_for_code(code)}`\n"
        markdown += f"`{get_report_form_for_code(code)}` | {description}\n"
    markdown += f"`{get_report_form_for_code('SpecialHandling')}` | Special Handling\n"

    return markdown


def malformed_error(message, heading="Malformed Recommendation"):
    markdown = f"""
    ### :x: {heading}

    {message}

    If you entered this set of inputs, your recommendation would not be actionable,
    and the safety net team would contact you and ask you to addended your report and
    create a correctly filled-out form.
    """

    st.error(markdown)
    st.stop()


if submit_button or st.session_state.show:
    try:
        start_days: int | None = int(start_days_str)
        end_days: int | None = int(end_days_str)
    except ValueError:
        start_days = None
        end_days = None
    if not modality:
        malformed_error("Please select a modality.")
    assert modality is not None
    if not body_part:
        malformed_error("Please select a body region.")
    if not start_days or not end_days:
        malformed_error("Please enter numbers for both start and end days.")
    if not start_days or not end_days or start_days >= end_days:
        malformed_error("End days must be greater than start days.")

    recommendable = get_recommendable(
        mappings, body_part, modality, laterality
    ) or get_fallback_recommendable(modality_mappings, modality)

    if not recommendable or recommendable == ADDITIONAL_IMAGING:
        malformed_error(SPECIAL_RECOMMENDABLES[ADDITIONAL_IMAGING])
    assert recommendable is not None

    if recommendable == LATERALITY_UNSPECIFIED:
        malformed_error("Need to specify laterality for this modality/body part.")

    st.info(get_markdown_for_recommendable(recommendable))
    recommendable_report_codes = get_report_codes_for_recommendable(
        report_codes, recommendable
    )

    st.markdown(get_markdown_for_report_codes(recommendable_report_codes))

    col1, col2 = st.columns([3, 1])
    with col1:
        """
        To use a report code, insert the report code text anywhere in the report or
        in the free text field of the Follow-up Recommendations dialog. The "Macro:
        Special" macro or "CSR Recommendables" Clinical Guidance module can be used
        to insert the report code text into the report.
        """

    with col2:
        st.page_link(
            "vid_report_code.py",
            label="Inserting Report Codes",
            icon=":material/movie:",
        )
