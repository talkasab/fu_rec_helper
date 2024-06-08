import streamlit as st

from constants import (
    BODY_PART_OPTIONS,
    MODALITY_OPTIONS,
    SPECIAL_HANDLING,
    SPECIAL_RECOMMENDABLES,
)
from utils import (
    get_code_and_mappings_for_unmapped_recommendable,
    get_fallback_recommendable,
    get_mappings_for_recommendable,
    get_recommendable,
    get_report_codes_for_recommendable,
    load_data,
)


# See https://discuss.streamlit.io/t/where-to-set-page-width-when-set-into-non-widescreeen-mode/959/15
def set_width_pixels(width: int):
    assert width >= 500 and width <= 1200, "Width must ≥500 and ≤ 1200."
    st.html(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: {width}px;
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
        "Report a Bug": None,
        "About": ABOUT_TEXT,
    },
)
set_width_pixels(1000)

mappings, report_codes, recommendables, modality_mappings = load_data()

st.title("CSR Action Helper")
st.write("Helper app to show radiologists how to recommend follow-up imaging at MGB.")

st.subheader("What Happens When I...?")
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
    markdown += f"- **{SPECIAL_HANDLING}**: `{{{{SpecialHandling}}}}`  \n{SPECIAL_RECOMMENDABLES[SPECIAL_HANDLING]}\n"
    for code, description in report_codes:
        markdown += f"- **{description}**: `{{{{{code}}}}}`\n"
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
            report_codes = get_report_codes_for_recommendable(
                report_codes, recommendable
            )
            st.markdown(get_markdown_for_report_codes(report_codes))
        else:
            st.write("No recommendation found.")

st.divider()
st.subheader("How Do I Recommend...?")
search_recommendable = st.selectbox(
    "Select a recommendable to see how to recommend it",
    recommendables[~(recommendables["Category"] == "special")]["Name"],
    index=None,
)
if search_recommendable:
    search_mappings = get_mappings_for_recommendable(mappings, search_recommendable)
    if not search_mappings.empty:
        st.write(f"Body part/modality combinations for **{search_recommendable}**:")
        st.dataframe(
            search_mappings,
            hide_index=True,
            column_config={
                "BodyPart": st.column_config.TextColumn(
                    label="Body Part", width="medium"
                ),
                "Modality": st.column_config.TextColumn(width="small"),
            },
        )
    else:
        code, search_mappings = get_code_and_mappings_for_unmapped_recommendable(
            mappings, report_codes, search_recommendable
        )
        st.write(f"Code for **{search_recommendable}**: `{{{{{code}}}}}`")
        st.write(
            "Use the code with any of the following body part/modality combinations:"
        )
        st.dataframe(
            search_mappings,
            hide_index=True,
            column_config={
                "BodyPart": st.column_config.TextColumn(
                    label="Body Part", width="medium"
                ),
                "Modality": st.column_config.TextColumn(width="small"),
            },
        )

st.divider()
st.subheader("Recommendable Exams")
with st.expander("Show all recommendable exams"):
    col1, _ = st.columns(2)
    category_filter = col1.multiselect(
        "Filter by category", recommendables["Category"].unique()
    )
    if category_filter:
        filtered_recommendables = recommendables[
            recommendables["Category"].isin(category_filter)
        ]
    else:
        filtered_recommendables = recommendables

    st.dataframe(
        filtered_recommendables,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Name": st.column_config.TextColumn(width="large"),
            "Category": st.column_config.TextColumn(width="small"),
            "Modality": st.column_config.TextColumn(width="small"),
            "Region": st.column_config.TextColumn(width="small"),
            "Code": st.column_config.TextColumn(width="medium"),
        },
    )
