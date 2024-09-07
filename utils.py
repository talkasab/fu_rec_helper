import re

import pandas as pd
import streamlit as st

from constants import (
    ADDITIONAL_IMAGING,
    FILE_NAMES,
    SPECIAL_HANDLING,
    SPECIAL_RECOMMENDABLES,
)


def normalize_string(in_string: str | None) -> str:
    assert in_string is not None
    out = in_string.lower()
    return re.sub(r"\W", "", out)


def get_code_for_recommendable(
    report_codes: pd.DataFrame, recommendable: str
) -> str | None:
    try:
        codes = report_codes[report_codes["InsertedRecommendable"] == recommendable][
            "code"
        ]
        return codes.iloc[0] if not codes.empty else None
    except IndexError:
        return None


def get_report_form_for_code(code: str) -> str:
    return "{REC:" + code + "}"


@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    mappings = pd.read_parquet(FILE_NAMES["mappings"])
    mappings.sort_index(inplace=True, na_position="first")
    report_codes = pd.read_parquet(FILE_NAMES["report_codes"])
    recommendables = pd.read_parquet(FILE_NAMES["recommendables"])
    modality_mappings = pd.read_parquet(FILE_NAMES["modality_mappings"])

    mapped_recommendables = mappings["Recommendable"].unique()
    report_code_recommendables = report_codes["InsertedRecommendable"].unique()

    def classify_recommendable(recommendable: str) -> str:
        if recommendable == SPECIAL_HANDLING:
            return "SpecialHandling"
        if (
            recommendable in mapped_recommendables
            or recommendable in SPECIAL_RECOMMENDABLES
        ):
            return "—"
        if recommendable in report_code_recommendables:
            code = get_code_for_recommendable(report_codes, recommendable)
            assert code is not None
            return code
        return "Unknown"

    recommendables["Code"] = recommendables["Name"].apply(classify_recommendable)
    return mappings, report_codes, recommendables, modality_mappings


def get_recommendables_df() -> pd.DataFrame:
    dfs = load_data()
    recommendables = dfs[2].query("Category != 'special'")
    return recommendables


def get_recommendable(
    mappings: pd.DataFrame,
    body_part: str | None,
    modality: str | None,
    laterality: str | None,
) -> str | None:
    if not body_part or not modality:
        return None
    body_part_norm = normalize_string(body_part)
    modality_norm = normalize_string(modality)
    laterality_norm = normalize_string(laterality) or "unspecified"
    try:
        value = mappings.loc[  # type: ignore
            (body_part_norm, modality_norm, laterality_norm), "Recommendable"
        ].to_list()  # type: ignore
        return value[0] if value else None
    except KeyError:
        return None


FALLBACK_RECOMMENDABLES = {
    "Radiology": ADDITIONAL_IMAGING,
    "Intervention": "Interventional Procedure Recommendation",
    "NonRadiology": "Non-Radiology Recommendation",
}


def get_fallback_recommendable(
    modality_mappings: pd.DataFrame, modality: str
) -> str | None:
    modality_norm = normalize_string(modality)
    try:
        cls = str(modality_mappings.loc[modality_norm, "Class"])
        return FALLBACK_RECOMMENDABLES[cls]
    except KeyError:
        return None


def get_report_codes_for_recommendable(
    report_codes: pd.DataFrame, recommendable: str
) -> list[tuple[str, str]]:
    try:
        return list(
            report_codes[report_codes["ReplaceRecommendable"] == recommendable][
                ["code", "InsertedRecommendable"]
            ].itertuples(index=False, name=None)
        )
    except KeyError:
        return []


def get_mappings_for_recommendable(
    mappings: pd.DataFrame, recommendable: str
) -> pd.DataFrame:
    result = mappings[
        (mappings["Recommendable"] == recommendable) & mappings["CoreModality"]
    ][["BodyPart", "Modality"]]
    # drop the index
    result.reset_index(drop=True, inplace=True)
    # get unique combinations of BodyPart, Modality, and Laterality
    result.drop_duplicates(inplace=True)
    return result


def get_code_and_mappings_for_unmapped_recommendable(
    mappings: pd.DataFrame, report_codes, recommendable: str
) -> tuple[str, pd.DataFrame]:
    code = get_code_for_recommendable(report_codes, recommendable)
    # Get the ReplaceRecommendables for the code
    replace_recommendables = report_codes[
        report_codes["InsertedRecommendable"] == recommendable
    ]["ReplaceRecommendable"].unique()
    # Get the mappings for each ReplaceRecommendable
    result = mappings[
        (mappings["Recommendable"].isin(replace_recommendables))
        & mappings["CoreModality"]
    ][["BodyPart", "Modality"]]
    # drop the index
    result.reset_index(drop=True, inplace=True)
    # get unique combinations of BodyPart, Modality, and Laterality
    result.drop_duplicates(inplace=True)
    assert code is not None
    return code, result
