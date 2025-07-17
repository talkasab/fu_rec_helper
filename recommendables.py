import pandas as pd
import streamlit as st

from utils import (
    get_code_and_mappings_for_unmapped_recommendable,
    get_mappings_for_recommendable,
    get_report_form_for_code,
    load_data,
)

mappings, report_codes, recommendables, modality_mappings = load_data()


def get_laterality(recommendable: str) -> str | None:
    # If the recommendable has the string "Left", "Right", or "Bilateral" return that string
    if "Left" in recommendable:
        return "Left"
    if "Right" in recommendable:
        return "Right"
    if "Bilateral" in recommendable:
        return "Bilateral"
    return None


def get_search_mappings_markdown(
    search_mappings: pd.DataFrame, laterality: str | None = None
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


def get_recommendable_from_query():
    query_recommendable = st.query_params.get("recommendable")
    if query_recommendable:
        st.session_state.update(recommendable=query_recommendable) # pyright: ignore[reportCallIssue]
    return query_recommendable


def get_selected_recommendable() -> str | None:
    rows = event.selection.rows  # type: ignore
    if not rows:
        return None
    selected_row = rows[0]
    recommendable = filtered_recommendables.iat[selected_row, 0]
    return recommendable


st.header("Recommendable Exams")

col1, col2 = st.columns(2)
category_filter = col1.multiselect(
    "Filter by category", recommendables["Category"].unique()
)
modality_filter = col2.multiselect(
    "Filter by modality", recommendables["Modality"].unique()
)
if category_filter and modality_filter:
    filtered_recommendables = recommendables[
        recommendables["Category"].isin(category_filter)
        & recommendables["Modality"].isin(modality_filter)
    ]
elif modality_filter:
    filtered_recommendables = recommendables[
        recommendables["Modality"].isin(modality_filter)
    ]
elif category_filter:
    filtered_recommendables = recommendables[
        recommendables["Category"].isin(category_filter)
    ]
else:
    filtered_recommendables = recommendables

event = st.dataframe(
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
    selection_mode="single-row",
    on_select="rerun",
)


selected_recommendable = get_selected_recommendable()
if selected_recommendable:
    st.query_params["recommendable"] = selected_recommendable
recommendable = get_recommendable_from_query()

DONT_SHOW_HOW_TO = [
    "Additional Imaging Needed",
    "Interventional Procedure Recommendation",
]
if recommendable and recommendable not in DONT_SHOW_HOW_TO:
    with st.container(border=True):
        show_how_to_recommend(recommendable)
else:
    st.info("Select a recommendable exam to see how to recommend it.")
