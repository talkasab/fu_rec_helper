import streamlit as st

from constants import (
    ADDITIONAL_IMAGING,
    BODY_PART_OPTIONS,
    INTERVENTIONAL_PROCEDURE,
    LATERALITY_UNSPECIFIED,
    MODALITY_OPTIONS,
    NON_RADIOLOGY,
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


def malformed_error(messages: list[str], heading="Malformed Recommendation"):
    message_list = "\n".join(f"- {m}" for m in messages)
    markdown = f"""
### :x: {heading}

{message_list}

If you entered this set of inputs, your recommendation would not be actionable,
and the safety net team would contact you and ask you to addended your report and
create a correctly filled-out form.
"""

    st.error(markdown)
    st.stop()


def parse_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


if submit_button or st.session_state.show:
    errors = []
    start_days = parse_int(start_days_str)
    end_days = parse_int(end_days_str)
    if not modality:
        errors.append("Please select a modality.")
    assert modality is not None
    if not body_part:
        errors.append("Please select a body region.")
    if start_days is None or end_days is None or start_days < 0 or end_days < 1:
        errors.append("Please enter positive numbers for both start and end days.")
    if start_days and end_days and start_days >= end_days:
        errors.append("End days must be greater than start days.")

    if body_part and modality:
        recommendable = get_recommendable(
            mappings, body_part, modality, laterality
        ) or get_fallback_recommendable(modality_mappings, modality)
    elif modality:
        recommendable = get_fallback_recommendable(modality_mappings, modality)
    else:
        recommendable = None

    if recommendable == ADDITIONAL_IMAGING:
        errors.append(SPECIAL_RECOMMENDABLES[ADDITIONAL_IMAGING])
    elif recommendable == LATERALITY_UNSPECIFIED:
        errors.append("Need to specify laterality for this modality/body part.")
    elif recommendable in [INTERVENTIONAL_PROCEDURE, NON_RADIOLOGY]:
        st.info(get_markdown_for_recommendable(recommendable))
        st.stop()

    if errors:
        malformed_error(errors)

    assert recommendable is not None
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
