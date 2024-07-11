import streamlit as st

from constants import (
    BODY_PART_OPTIONS,
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

st.header("What Happens When I...?")
st.write(
    "Select a body part, modality, and laterality to see what exams are recommended."
)
with st.form(key="my_form"):
    body_part = st.selectbox("Body Part", BODY_PART_OPTIONS, format_func=lambda x: x)
    modality = st.selectbox("Modality", MODALITY_OPTIONS)
    laterality = st.selectbox(
        "Laterality", ["", "Left", "Right", "Bilateral", "Unspecified", "Unilateral"]
    )
    submit_button = st.form_submit_button(label="Show Recommendation")


def get_markdown_for_recommendable(recommendable: str):
    markdown = f"#### :arrow_forward: Recommendation: **{recommendable}**\n"
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


if submit_button:
    if not modality:
        st.error("Please select a modality.")
    else:
        recommendable = get_recommendable(
            mappings, body_part, modality, laterality
        ) or get_fallback_recommendable(modality_mappings, modality)
        if recommendable:
            st.info(get_markdown_for_recommendable(recommendable))
            recommendable_report_codes = get_report_codes_for_recommendable(
                report_codes, recommendable
            )
            st.markdown(get_markdown_for_report_codes(recommendable_report_codes))
        else:
            st.write("No recommendation found.")
