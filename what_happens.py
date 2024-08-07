import streamlit as st

from constants import (
    ADDITIONAL_IMAGING,
    BODY_PART_OPTIONS,
    LATERALITY_UNSPECIFIED,
    MODALITY_OPTIONS,
    SPECIAL_HANDLING,
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

"""Select a body part, modality, and laterality to see what exams are recommended.

Remember to use distinct start and end days for the recommendation!
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
    markdown = "#### :mag: Report Codes\n"
    markdown += (
        f"- **{SPECIAL_HANDLING}**: `{get_report_form_for_code('SpecialHandling')}`  \n"
    )
    markdown += SPECIAL_RECOMMENDABLES[SPECIAL_HANDLING] + "\n"
    for code, description in report_codes:
        markdown += f"- **{description}**: `{get_report_form_for_code(code)}`\n"
    return markdown


if submit_button or st.session_state.show:
    try:
        start_days: int | None = int(start_days_str)
        end_days: int | None = int(end_days_str)
    except ValueError:
        start_days = None
        end_days = None
    # set_query_from_state()
    if not modality:
        st.error("Please select a modality.")
    elif not body_part:
        st.error("Please select a body region.")
    elif not start_days or not end_days:
        st.error("Please enter numbers for both start and end days.")
    else:
        if not start_days or not end_days or start_days >= end_days:
            st.error("End days must be greater than start days.")
        else:
            recommendable = get_recommendable(
                mappings, body_part, modality, laterality
            ) or get_fallback_recommendable(modality_mappings, modality)
            if recommendable:
                if recommendable in (ADDITIONAL_IMAGING, LATERALITY_UNSPECIFIED):
                    st.warning(
                        get_markdown_for_recommendable(recommendable, icon="warning")
                    )
                else:
                    st.info(get_markdown_for_recommendable(recommendable))
                recommendable_report_codes = get_report_codes_for_recommendable(
                    report_codes, recommendable
                )
                st.markdown(get_markdown_for_report_codes(recommendable_report_codes))
            else:
                st.write("No recommendation found.")
