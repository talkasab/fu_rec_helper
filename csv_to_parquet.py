import numpy as np
import pandas as pd

from constants import CORE_MODALITIES


def load_mappings(filename: str) -> pd.DataFrame:
    # Load the mappings file using pyarrow data types:
    # - Ignore the RecID column
    # - BodyPart, Modality, and Laterality should be categories
    # - Turn BodyPart and Modality and Laterality columns into normalized strings--no whitespace or special characters, all lowercase
    # - Recommendable should be a string
    # - Drop the RecID column
    df = pd.read_csv(
        filename,
        sep="|",
        dtype={
            "BodyPart": "str",
            "Modality": "str",
            "Laterality": "str",
            "Recommendable": "str",
        },
    )
    df["BodyPartNorm"] = df["BodyPart"].str.lower().str.replace(r"\W", "", regex=True)
    df["ModalityNorm"] = df["Modality"].str.lower().str.replace(r"\W", "", regex=True)
    df["LateralityNorm"] = (
        df["Laterality"].str.lower().str.replace(r"\W", "", regex=True)
    )
    df["BodyPart"] = df["BodyPart"].astype("category")
    df["Modality"] = df["Modality"].astype("category")
    df["Laterality"] = df["Laterality"].astype("category")
    df["BodyPartNorm"] = df["BodyPartNorm"].astype("category")
    df["ModalityNorm"] = df["ModalityNorm"].astype("category")
    df["LateralityNorm"] = df["LateralityNorm"].astype("category")
    df["Recommendable"] = df["Recommendable"].astype("category")
    # Make the index be a composite of BodyPartNorm, ModalityNorm, and LateralityNorm
    df.set_index(["BodyPartNorm", "ModalityNorm", "LateralityNorm"], inplace=True)
    # Drop the RecID column
    df = df.drop(columns=["RecID"])
    df["CoreModality"] = df["Modality"].isin(CORE_MODALITIES)
    return df


def load_modality_mappings(filename: str) -> pd.DataFrame:
    # Load the mappings file using pyarrow data types:
    # - Ignore the RecID column
    # - Modality should be a category
    # - Turn Modality column into normalized strings--no whitespace or special characters, all lowercase
    # - Drop the RecID column
    df = pd.read_csv(filename, dtype={"Modality": "str"})
    df["ModalityNorm"] = df["Modality"].str.lower().str.replace(r"\W", "", regex=True)
    df["Modality"] = df["Modality"].astype("category")
    df["ModalityNorm"] = df["ModalityNorm"].astype("category")
    # Make the index be a composite of BodyPartNorm, ModalityNorm, and LateralityNorm
    df.set_index(["ModalityNorm"], inplace=True)
    # Drop the RecID column
    df = df.drop(columns=["ID", "MapTo", "Active"])
    # Drop the row with a missing Modality name
    df = df.dropna(subset=["Modality"])
    return df


def load_report_codes(filename) -> pd.DataFrame:
    # Load the mappings file using pyarrow data types
    # Leave out the inserted_id and replace_id columns
    # Rename inserted_recommendable to InsertedRecommendable and replace_recommendable to ReplaceRecommendable
    # Make InsertedRecommendable and ReplaceRecommendable categories
    df = pd.read_csv(
        filename,
        sep="|",
        dtype={
            "inserted_recommendable": "str",
            "replace_recommendable": "str",
        },
    )
    df["InsertedRecommendable"] = df["inserted_recommendable"].astype("category")
    df["ReplaceRecommendable"] = df["replace_recommendable"].astype("category")
    df = df.drop(
        columns=[
            "inserted_id",
            "replace_id",
            "inserted_recommendable",
            "replace_recommendable",
        ]
    )
    return df


def load_recommendables(filename: str) -> pd.DataFrame:
    # Load the mappings file using pyarrow data types
    df = pd.read_csv(
        filename,
        usecols=["name", "category", "modality", "region"],
    )
    df["Name"] = df["name"].astype("category")
    df["Category"] = df["category"].astype("category")
    df["Modality"] = df["modality"].astype("category")
    df["Region"] = df["region"].astype("category")
    df = df.drop(columns=["name", "category", "modality", "region"])
    return df


def create_report_code_info(
    report_codes: pd.DataFrame, recommendables: pd.DataFrame
) -> pd.DataFrame:
    # get a new df with just the unique inserted recommendables and their report codes
    unique_inserted_recommendables = report_codes.drop_duplicates(
        subset=["InsertedRecommendable"]
    )[["code", "InsertedRecommendable"]]
    report_code_info = unique_inserted_recommendables.merge(
        recommendables, left_on="InsertedRecommendable", right_on="Name"
    )
    report_code_info.drop(columns=["Name"], inplace=True)
    # If code is Venogram, WithContrast, or Arthrogram, set Category to "special", and Modality and Region to NaN
    report_code_info.loc[
        report_code_info["code"].isin(["Venogram", "WithContrast", "Arthrogram"]),
        ["Category", "Modality", "Region"],
    ] = ["special", np.nan, np.nan]
    return report_code_info


if __name__ == "__main__":
    modality_mappings = load_modality_mappings("data/modality_mappings.csv")
    modality_mappings.to_parquet("data/modality_mappings.parquet")
    mappings = load_mappings("data/body_part_modality_laterality_recommendable.csv")
    mappings.to_parquet("data/body_part_modality_laterality_recommendable.parquet")
    report_codes = load_report_codes("data/report_codes.csv")
    report_codes.to_parquet("data/report_codes.parquet")
    recommendables = load_recommendables("data/recommendables.csv")
    recommendables.to_parquet("data/recommendables.parquet")
    report_code_info = create_report_code_info(report_codes, recommendables)
    report_code_info.to_csv("data/report_code_info.csv", index=False)
