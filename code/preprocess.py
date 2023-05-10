import os
from jsonlines_wl import jsonlines_wl, splits
from ncc_to_heads import get_heads

VERSION = 1.0
data_path = os.path.join(f"data/v{VERSION}/")

JSONLINES_DOCWISE = os.path.join(data_path, "narc_jsonl")
JSONLINES_WL = os.path.join(data_path, "narc_wordlevel")

NAME_CORE = "narc" # First part of wl-formatted filenames

print(f"Data source: {data_path}")

paths = {
    "bokmaal": os.path.join(data_path, "annotated_bokmaal")
}

print(f"Parsing jsonlines for word-level coreference...")
jsonlines_wl(JSONLINES_DOCWISE, JSONLINES_WL, name_core=NAME_CORE)
print(f"Splitting data...")
splits(JSONLINES_WL, split_splits = (0.8, 0.9), name_core=NAME_CORE)
print(f"Getting heads for word-level coreference...")
get_heads(JSONLINES_WL, NAME_CORE)
