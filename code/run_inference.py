# Make sure we have files without clusters information for testing the model.

import jsonlines
import os

gold_source = "/fp/homes01/u01/ec-egilron/narc-baseline/data/wl-formatted"
inference_source_folder = "/fp/homes01/u01/ec-egilron/narc-baseline/data/inference"
predicted_folder = "/fp/homes01/u01/ec-egilron/narc-baseline/experiments/outputs"
wl_naming = {"dev":"development", "test":"test"}
source_filenames = ["narc_development.jsonl", "narc_test.jsonl"]
inference_source_filenames = ["narc_dev_unlabelled.jsonl", "narc_test_unlabelled.jsonl"]
predict_py_path = "/fp/homes01/u01/ec-egilron/narc-baseline/wl-coref-ncc/predict.py"


# def read_clusters(source_path:str, key="clusters"):
#     """ read the clusters from multiline jsonlines,
#     return list of clusters """
#     with jsonlines.open(source_path) as rf:
#         clusters = [doc[key] for doc in rf]
#     return clusters

# This should probably be moved to the data conversion scripts
if not os.path.exists(inference_source_folder):
    os.mkdir(inference_source_folder)
for source_f, inf_f in zip(source_filenames,inference_source_filenames ):
    source_path = os.path.join(gold_source, source_f)
    inference_source_path = os.path.join(inference_source_folder, inf_f)
    with jsonlines.open(source_path, mode="r") as source:
        inf_source = [{"document_id":d["document_id"], 
                        "cased_words": d["cased_words"],
                        "sent_id": d["sent_id"]
                        } for d in source]
    with jsonlines.open(inference_source_path, mode="w") as wf:
        wf.write_all(inf_source)
            
    



for experiment in ["POC2_000", "POC2_001"]:
    for inf_f in inference_source_filenames:
        inference_source_path = os.path.join(inference_source_folder, inf_f)
        predicted_path = os.path.join(predicted_folder, f"predicted_{experiment}_{inf_f}")
        scriptline = f"python {predict_py_path} {experiment} {inference_source_path} {predicted_path} --config-file /fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC2.toml"
        print()
        print(scriptline)
print()
        

# python wl-coref-ncc/predict.py POC2_000 data/wl-formatted/narc_development.jsonl POC2_000_dev_predicted.jsonlines --config-file experiments/tomls/POC2.toml

"""
python /fp/homes01/u01/ec-egilron/narc-baseline/wl-coref-ncc/predict.py POC2_000 /fp/homes01/u01/ec-egilron/narc-baseline/data/inference/narc_dev_unlabelled.jsonl /fp/homes01/u01/ec-egilron/narc-baseline/experiments/outputs/predicted_POC2_000_narc_dev_unlabelled.jsonl --config-file /fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC2.toml

python /fp/homes01/u01/ec-egilron/narc-baseline/wl-coref-ncc/predict.py POC2_000 /fp/homes01/u01/ec-egilron/narc-baseline/data/inference/narc_test_unlabelled.jsonl /fp/homes01/u01/ec-egilron/narc-baseline/experiments/outputs/predicted_POC2_000_narc_test_unlabelled.jsonl --config-file /fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC2.toml

python /fp/homes01/u01/ec-egilron/narc-baseline/wl-coref-ncc/predict.py POC2_001 /fp/homes01/u01/ec-egilron/narc-baseline/data/inference/narc_dev_unlabelled.jsonl /fp/homes01/u01/ec-egilron/narc-baseline/experiments/outputs/predicted_POC2_001_narc_dev_unlabelled.jsonl --config-file /fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC2.toml

python /fp/homes01/u01/ec-egilron/narc-baseline/wl-coref-ncc/predict.py POC2_001 /fp/homes01/u01/ec-egilron/narc-baseline/data/inference/narc_test_unlabelled.jsonl /fp/homes01/u01/ec-egilron/narc-baseline/experiments/outputs/predicted_POC2_001_narc_test_unlabelled.jsonl --config-file /fp/homes01/u01/ec-egilron/narc-baseline/experiments/tomls/POC2.toml
"""