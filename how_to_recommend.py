import streamlit as st

from utils import (
    get_code_and_mappings_for_unmapped_recommendable,
    get_mappings_for_recommendable,
    get_report_form_for_code,
    load_data,
)

mappings, report_codes, recommendables, modality_mappings = load_data()

st.header("How Do I Recommend...?")
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
        st.write(
            f"Code for **{search_recommendable}**: `{get_report_form_for_code(code)}`"
        )
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
