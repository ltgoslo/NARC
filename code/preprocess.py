import os
from conversion.gather_annotations import gather
from conversion.batch_ann2jsonlines import convert as ann2jsonlines
from jsonlines_wl import jsonlines_wl, splits
from ncc_to_heads import get_heads

VERSION = 0.1
data_path = os.path.join(f"data/v{VERSION}/")
parsed_path = os.path.join(data_path, "parsed")

ANN_FOLDER = os.path.join(parsed_path, "ann")
JSONLINES_DOCWISE = os.path.join(parsed_path, "jsonl")
JSONLINES_WL = os.path.join(parsed_path, "wordlevel")

NAME_CORE = "narc" # First part of wl-formatted filenames

print(f"Data source: {data_path}")

paths = {
    "bokmaal": os.path.join(data_path, "annotated_bokmaal")
}

for variation, source_path in paths.items():
    print(f"Gathering annotated files from {source_path}")
    gather(
        source_folder=source_path,
        output_folder=ANN_FOLDER,
        variation=variation
    )

print(f"Converting .ann to .jsonl...")
ann2jsonlines(source_path=ANN_FOLDER, output_path=JSONLINES_DOCWISE)
print(f"Parsing jsonlines for word-level coreference...")
jsonlines_wl(JSONLINES_DOCWISE, JSONLINES_WL, name_core=NAME_CORE)
print(f"Splitting data...")
splits(JSONLINES_WL, split_splits = (0.8, 0.9), name_core=NAME_CORE)
print(f"Getting heads for word-level coreference...")
get_heads(JSONLINES_WL, NAME_CORE)
