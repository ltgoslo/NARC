# converts the already ann->jsonlines converted files into .conll
import argparse
import json
import os

from conversion import textpos2sentpos, write_chains, write_file

def convert(args: argparse.Namespace):
    source_path = os.path.join(os.getcwd(), args.folder)
    if not os.path.exists(source_path):
        raise FileNotFoundError(
            f"No annotation files found in folder: {args.folder}"
        )
        
    parse_path = os.path.join(os.getcwd(), "annotations_conll")
    if not os.path.exists(parse_path):
        print("Creating folder for parsed files...")
        os.mkdir(parse_path)

    jsonlines = [f for f in os.listdir(source_path) if ".jsonl" in f]
    for jsonline in jsonlines:
        jsonline_path = os.path.join(source_path, jsonline)
        with open(jsonline_path, "r", encoding="utf-8") as jsonline_file:
            data = json.load(jsonline_file)

        docs = {}
        doc_key = data["doc_key"]
        # sents = [
        #     [list(token) for token in zip(*sent)]
        #     for sent in data["sentences"]
        # ]
        sents = [
            # token is just right: a tuple of col
            [list(token) for token in zip(*sent)]
            # sent is: [ sent1_tokens, sent2_speakers,... ]
            for sent in zip(*[iter(data[col]) for col in ["sentences"]])
        ]
        # sents = [[list(t) for t in sent] for sent in data["sentences"]]

        chains = data["clusters"]

        mentions = [m for chain in chains for m in chain]
        textpos2sentpos(mentions, sents)

        write_chains(sents, chains, append=True)

        docs[doc_key] = sents

        conll_path = os.path.join(parse_path, jsonline.split(".")[0] + ".conll")
        write_file(fpath=conll_path, docs=docs)

if __name__ == "__main__":
    if ".git" not in os.listdir(os.path.abspath(os.curdir)):
        raise EnvironmentError("Needs to run from project root")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder",
        type=str,
        default="annotations_jsonlines",
        help="folder containing .jsonl files"
    )
    
    convert(parser.parse_args())
