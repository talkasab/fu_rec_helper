import pandas as pd
import streamlit as st

from utils import get_recommendables_df

recommendables: pd.DataFrame = get_recommendables_df()

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
