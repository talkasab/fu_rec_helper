"""Take a new TSV mapping file and update our parquet mapping file."""

from pathlib import Path
from sys import argv
from typing import NamedTuple

import pandas as pd

from constants import CORE_MODALITIES

MAPPING_FILE = Path("data/body_part_modality_laterality_recommendable.parquet")


def load_existing_mapping() -> pd.DataFrame:
    if not MAPPING_FILE.exists():
        raise FileNotFoundError(f"Mapping file {MAPPING_FILE} not found.")
    return pd.read_parquet(MAPPING_FILE)


def load_new_mapping(filename: str) -> pd.DataFrame:
    update_file = Path(filename)
    if not update_file.exists():
        raise FileNotFoundError(f"Update file {update_file} not found.")
    updated = pd.read_csv(update_file, delimiter="|")
    updated["BodyPartNorm"] = (
        updated["BodyPart"].str.lower().str.replace(r"\W", "", regex=True)
    )
    updated["ModalityNorm"] = (
        updated["Modality"].str.lower().str.replace(r"\W", "", regex=True)
    )
    updated["LateralityNorm"] = (
        updated["Laterality"].str.lower().str.replace(r"\W", "", regex=True)
    )
    updated.set_index(["BodyPartNorm", "ModalityNorm", "LateralityNorm"], inplace=True)
    updated["CoreModality"] = updated["Modality"].isin(CORE_MODALITIES)
    updated.drop(columns=["RecommendableID"], inplace=True)
    return updated


def check_recommendable(row):
    try:
        existing_row = existing.loc[row.name].iloc[0]
        if existing_row["Recommendable"] == row["Recommendable"]:
            return "Same"
        else:
            return "Changed"
    except KeyError:
        return "New"


class ComparedMappingResult(NamedTuple):
    changed: pd.DataFrame
    new: pd.DataFrame


def find_changed_mappings(
    existing: pd.DataFrame, updated: pd.DataFrame
) -> ComparedMappingResult:
    if "Status" not in updated.columns:
        updated["Status"] = pd.Categorical(
            ["Same"] * len(updated), categories=["Same", "New", "Changed"]
        )
    # Apply the function to each row in updated
    updated["Status"] = updated.apply(check_recommendable, axis=1)
    # Display the rows where Recommendable does not match
    changed = updated[updated["Status"] == "Changed"]
    new = updated[updated["Status"] == "New"]
    return ComparedMappingResult(changed, new)


def find_deleted_mappings(
    existing: pd.DataFrame, updated: pd.DataFrame
) -> set[tuple[str, str, str]]:
    existing_set = set(existing.index)
    updated_set = set(updated.index)
    deleted = existing_set - updated_set
    return deleted


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <update_file>")
        exit(1)
    updated = load_new_mapping(argv[1])
    existing = load_existing_mapping()

    changed, new = find_changed_mappings(existing, updated)
    deleted = find_deleted_mappings(existing, updated)

    print(f"Changed mappings ({len(changed)})")
    print(changed["Recommendable"])

    print(f"New mappings ({len(new)})")
    print(new["Recommendable"])

    print(f"Deleted mappings {len(deleted)}")
    [print(f"  {deleted_row}") for deleted_row in deleted]

    # Save the updated mapping
    updated.to_parquet(MAPPING_FILE)
