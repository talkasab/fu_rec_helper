import streamlit as st
from pandas import DataFrame

from utils import (
    get_code_and_mappings_for_unmapped_recommendable,
    get_mappings_for_recommendable,
    get_report_form_for_code,
    load_data,
)

mappings, report_codes, recommendables, modality_mappings = load_data()


def get_search_mappings_markdown(
    search_mappings: DataFrame, laterality: str | None = None
) -> str:
    if laterality:
        markdown = "Modality | Body Part | Laterality\n"
        markdown += "--------- | -------- | ----------\n"
        for index, row in search_mappings.iterrows():
            markdown += f"{row['Modality']} | {row['BodyPart']} | {laterality}\n"
        return markdown

    markdown = "Modality | Body Part \n"
    markdown += "--------- | --------\n"
    for index, row in search_mappings.iterrows():
        markdown += f"{row['Modality']} | {row['BodyPart']}\n"
    return markdown


def set_state_from_query():
    query_recommendable = st.query_params.get("recommendable")
    if query_recommendable:
        st.session_state.update(recommendable=query_recommendable)


def set_query_from_state():
    if st.session_state.recommendable:
        st.query_params.recommendable = st.session_state.recommendable


# def set_submitted_state():
#     state = st.session_state.to_dict()
#     print(state)
#     set_query_from_state()
#     st.session_state.submitted = True


def get_laterality(recommendable: str) -> str | None:
    # If the recommendable has the string "Left", "Right", or "Bilateral" return that string
    if "Left" in recommendable:
        return "Left"
    if "Right" in recommendable:
        return "Right"
    if "Bilateral" in recommendable:
        return "Bilateral"
    return None


def show_how_to_recommend(recommendable: str):
    laterality = get_laterality(recommendable)
    search_mappings = get_mappings_for_recommendable(mappings, recommendable)
    st.markdown(f"### To Recommend {recommendable}")
    if not search_mappings.empty:
        st.markdown(
            "Choose one of the below modality/body part combinations in the Follow-up Recommendations tool:"
        )
        st.markdown(get_search_mappings_markdown(search_mappings, laterality))
    else:
        code, search_mappings = get_code_and_mappings_for_unmapped_recommendable(
            mappings, report_codes, recommendable
        )
        col1, col2 = st.columns(2)
        with col1:
            st.write(f":warning: **Code required**: `{get_report_form_for_code(code)}`")
        with col2:
            st.page_link(
                "vid_report_code.py",
                label="Inserting a Report Code",
                icon=":material/movie:",
            )
        st.write(
            "Put the code in the report text, and activate the Follow-up Recommendations tool with one of the following modality/body part combinations:"
        )
        st.markdown(get_search_mappings_markdown(search_mappings, laterality))


if not hasattr(st.session_state, "submitted"):
    set_state_from_query()

st.header("How Do I Recommend...?")
search_recommendable = st.selectbox(
    "Select a recommendable to see how to recommend it",
    recommendables[~(recommendables["Category"] == "special")]["Name"],
    index=None,
    key="recommendable",
    on_change=set_query_from_state,
)


if search_recommendable:
    search_mappings = get_mappings_for_recommendable(mappings, search_recommendable)
    laterality = get_laterality(search_recommendable)
    if not search_mappings.empty:
        st.write(f"Body part/modality combinations for **{search_recommendable}**:")
        st.markdown(get_search_mappings_markdown(search_mappings, laterality))
    else:
        code, search_mappings = get_code_and_mappings_for_unmapped_recommendable(
            mappings, report_codes, search_recommendable
        )
        st.write(
            f"Code for **{search_recommendable}**: `{get_report_form_for_code(code)}`"
        )
        st.write(
            "Use the code with any of the following body part/modality combinations:"
        )
        st.markdown(get_search_mappings_markdown(search_mappings, laterality))
