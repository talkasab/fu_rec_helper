import pandas as pd
import streamlit as st

from how_to_recommend import show_how_to_recommend
from utils import get_recommendables_df

recommendables: pd.DataFrame = get_recommendables_df()


def get_recommendable_from_query():
    query_recommendable = st.query_params.get("recommendable")
    if query_recommendable:
        st.session_state.update(recommendable=query_recommendable)
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

if recommendable:
    with st.container(border=True):
        show_how_to_recommend(recommendable)
else:
    st.info("Select a recommendable exam to see how to recommend it.")
