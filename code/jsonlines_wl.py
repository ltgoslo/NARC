import os, random
import json, jsonlines
import spacy



# Convert the data into the jsonlines format used in wl-coref
def jsonlines_wl(source_folder, dest_folder, spacy_id="nb_core_news_sm",name_core="narc" ):
    nlp = spacy.load(spacy_id)
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    source_filenames = [f for f in os.listdir(source_folder) if ".json" in f]

    wl_formatted = []
    for idx, f_name in enumerate(source_filenames):
        with open (os.path.join(source_folder, f_name), encoding="utf8") as rf:
            # assert len(rf.readlines()) == 1
            # print(f_name)
            doc = json.loads(rf.readline().strip())
        wl_data = {
            "document_id": "nw"+doc["doc_key"], 
            "cased_words" : [t for s in doc["sentences"] for t in s],
            "sent_id" : [i for i, s in enumerate(doc["sentences"] )for t in s], 
            "part_id" : idx,
            "speaker": ["blank" for s in doc["sentences"] for t in s],
            "head": [None for s in doc["sentences"] for t in s],
            # Change this to real head when possible
            "clusters": []
        }
        docs = nlp.pipe([" ".join(wl_data["cased_words"])])
        heads = [token.head.i for token in next(iter(docs))]
        # Spacy gives heads its own index as head. wl-coref wants Null
        heads = [None if n == b else b for n, b in enumerate(heads) ]
        wl_data["head"] = heads
        
        for cluster in doc["clusters"]: # Add 1 to end word-index
            wl_data["clusters"].append( [[s,e+1] for s,e in cluster] ) # wl-coref creates range() with start and end
        wl_formatted.append(wl_data)

        # These should now be similar to the output of convert_to_jsonlines.py in wl-coref
        with jsonlines.open(os.path.join(dest_folder,f'{name_core}_all.jsonl'), 'w') as wf:
            wf.write_all(wl_formatted)
    print(f"Saved {len(wl_formatted)} documents into {dest_folder} ")

def splits(source_folder, split_splits = (0.7, 0.85), name_core="narc"):
    # creates copies in subfolders
    source_path = os.path.join(source_folder,f'{name_core}_all.jsonl') 
    with jsonlines.open(source_path) as rf:
        wl_formatted = [l for l in rf]
    
    # document_ids = [l["document_id"] for l in wl_formatted]
    # document_prefixes = set([d_id[:d_id.find("_")+3] for d_id in document_ids]) # Include first two letters after first underscore
    random.shuffle(wl_formatted)
    train_max = int(len(wl_formatted)*split_splits[0])
    dev_max = int(len(wl_formatted)*split_splits[1])
    _splits = {
        "train":wl_formatted[:train_max],
        "development": wl_formatted[train_max:dev_max],
        "test":wl_formatted[dev_max:]
    }
    for split, data in _splits.items():
        print(split,len(data))
        with jsonlines.open(os.path.join(source_folder,f'{name_core}_{split}.jsonl'), 'w') as wf:
            wf.write_all(data)

# source_folder = "annotations_jsonline"
# dest_folder = "wl-coref"
# spacy_id = "nb_core_news_sm"
# split_splits = (0.7, 0.85) 