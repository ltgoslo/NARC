# Read jsonlines files predicted with wl-coref and evaluate them with coreference-eval
# coreference-eval presently requires python 3.9

import corefeval
import jsonlines
import os

gold_folder = "/home/egil/gits_wsl/narc-baseline/data/wl-formatted"
gold_filenames = {"dev": "narc_development.jsonl", "test": "narc_test.jsonl"} 
predicted_folder = "/home/egil/gits_wsl/narc-baseline/experiments/outputs"



def read_clusters(source_path:str, key="clusters"):
    """ read the clusters from multiline jsonlines,
    return list of clusters """
    with jsonlines.open(source_path) as rf:
        clusters = [doc[key] for doc in rf]
    return clusters

to_score = os.listdir(predicted_folder)

for prediction in to_score:
    if "_dev" in prediction:
        gold_path = os.path.join(gold_folder, gold_filenames["dev"])
    else:
        gold_path = os.path.join(gold_folder, gold_filenames["test"])
    pred_path = os.path.join(predicted_folder, prediction)
    


    pred_split = prediction.split("_")
    experiment = pred_split[1]+"_"+str(pred_split[2])
    split = prediction.split("_")[-2]
    # print(gold_path, os.path.exists(gold_path))
    # print(pred_path, os.path.exists(predicted_folder))
    # print(experiment, split)

    gold_clusters = read_clusters(gold_path)
    pred_clusters = read_clusters(pred_path, key="span_clusters" )

    assert len(gold_clusters) == len(pred_clusters) # Should be one for each document

    scorer = corefeval.Scorer()
    for gold_doc, pred_doc in zip(gold_clusters, pred_clusters):
        # print(all([g==p for gold_c, pred_c in zip(gold_doc, pred_doc) 
        #                     for g,p in zip(gold_c, pred_c)]))
        scorer.update(corefeval.Document(predicted = pred_doc, truth = gold_doc))
    
    conll_f1, metrics = scorer.detailed_score(experiment, split)
    # Feiler, har fire, ikke tre listenivåer: [[[[1, 3], [26, 27], [
    # corefeval.get_metrics(pred_clusters, gold_clusters)
    print(conll_f1)
    print(metrics)



# for experiment in ["POC2_000", "POC2_001"]:
#     for split in ["dev", "test"]:
#         gold_path = os.path.join(gold_folder, f"narc_{wl_naming[split]}.jsonl")
#         pred_path = os.path.join(predicted_folder, f"{experiment}_{split}_predicted.jsonlines")
        
#         for f in [gold_path, pred_path]:
#             assert os.path.exists(f)
#         gold_clusters = read_clusters(gold_path)
#         pred_clusters = read_clusters(pred_path )

#         assert len(gold_clusters) == len(pred_clusters) # Should be one for each document
        

#         scorer = corefeval.Scorer()
#         for gold_doc, pred_doc in zip(gold_clusters, pred_clusters):
#             print(all([g==p for gold_c, pred_c in zip(gold_doc, pred_doc) 
#                                 for g,p in zip(gold_c, pred_c)]))
#             scorer.update(corefeval.Document(predicted = pred_doc, truth = gold_doc))
        
#         conll_f1, metrics = scorer.detailed_score(experiment, split)
#         # Feiler, har fire, ikke tre listenivåer: [[[[1, 3], [26, 27], [
#         # corefeval.get_metrics(pred_clusters, gold_clusters)
#         print(conll_f1)
#         print(metrics)

