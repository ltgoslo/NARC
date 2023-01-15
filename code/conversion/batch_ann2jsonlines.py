import json
import os

from conversion.ann_transform import convert_coref
from conversion.utils import make_jsonline

def convert(source_path, output_path, verbose=0):
    if not os.path.exists(source_path):
        raise FileNotFoundError(
            f"No annotation files found in path: {source_path}"
        )
    if not os.path.exists(output_path):
        print("Creating folder for parsed files...")
        os.mkdir(output_path)
        
    parsed_data = []
    for file in os.listdir(source_path):
        # just use the .ann files and fetch the text
        # during the parsing phase (by id ref)
        if ".txt" in file:
            continue
        file_path = os.path.join(source_path, file)

        if verbose > 0:
            print("Loading ", file_path)

        sentences, tokens, clusters = convert_coref(from_file=file_path)
        doc_key = file.split(".")[0]

        parsed_data.append(make_jsonline(
            doc_key, sentences, tokens, clusters
        ))

    for jsonline in parsed_data:
        jsonline_path = os.path.join(
            output_path, jsonline["doc_key"] + ".jsonl"
        )
        with open(jsonline_path, "w", encoding="utf-8") as jsonline_file:
            json.dump(jsonline, jsonline_file, ensure_ascii=False)