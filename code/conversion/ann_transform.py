from typing import List, Set, Tuple

from coref_types import (CorefClusters, Markable, MarkableGroup,
                         MarkableReference, Sentences, Tokens)
from utils import char_to_word_index, create_character_map, mark_to_idx, expand_child


def get_references(ann_data: Tokens) -> Tuple[Markable, List[MarkableReference]]:
    """ convert the raw ann data to referential objects

    Args:
        ann_data (Tokens): raw data from .ann file
    Returns:
        Tuple[Markable, List[MarkableReference]]:
            a dictionary of markable items and a list of coreferences
    """
    markables = {}
    corefs = []

    for line in ann_data:
        try:
            _id, ref_data, text = line.split("\t")
            
            if "R" in _id:
                _type, arg1, arg2 = ref_data.split()
                # ignore bridging
                if _type != "Bridging":
                    # return only the markable reference (T[x]) out of the Arg:T[x]
                    corefs.append((arg1.split(":")[-1], arg2.split(":")[-1]))

            else:
                links = ref_data.split()
                markables[_id] = {
                    "start": links[1],  # index 0 is simply "Markable"
                    "end": links[-1],
                    "text": text
                }

        except ValueError as err:
            print(f"Failed to read {line}: {err} -- Ignoring and continuing")
            continue

    return markables, corefs

def group_mentions(
    markables: Markable,
    references: List[MarkableReference]) -> List[MarkableGroup]:
    """ group a list of markables into their respective clusters

    Args:
        markables (dict[Markable]): mapping of a T[x] to start/end character index
        references (List[MarkableReference]): flat list of markable references

    Returns:
        List[MarkableReference]: a dict grouped with the start/end indices of markables
    """
    markable_coref_map = {}
    for mark in markables.keys():
        mark_refs = []
        for coref in references:
            if mark in coref:
                mark_refs.extend([ref for ref in coref if ref != mark])
        if len(mark_refs) > 0:
            markable_coref_map[mark] = mark_refs
            
    
    visited: Set[str] = set()
    entity_groups: List[List[str]] = []
    for entity in markable_coref_map:
        entity_group: Set[str] = set()
        expand_child(markable_coref_map, visited, entity, entity_group)
        if len(entity_group) > 0:
            # sort before converting to character index, preserving the original annotation order
            entity_groups.append(sorted(list(entity_group), key=lambda x: int(x.split("T")[-1])))

    idxs = []
    for group in entity_groups:
        idxs.append(tuple(mark_to_idx(markables, markable) for markable in group))
    return idxs
            
def get_reference_content(
    from_file: str) -> List[MarkableGroup]:

    if ".ann" not in from_file:
        raise FileNotFoundError("No .ann file provided")

    with open(from_file, "r", encoding="utf-8") as ann:
        markables, corefs = get_references(ann.readlines())
        grouped_mentions = group_mentions(
            markables=markables,
            references=corefs
        )
    
    return grouped_mentions
    

def get_text_content(from_file: str) -> Tuple[Sentences, Tokens]:
    # get the corresponding txt file
    txt_path = from_file.split(".ann")[0] + ".txt"
    
    with open(txt_path, "r", encoding="utf-8") as txt:
        text_data = "".join(txt.readlines())
        # replace double newlines by a single token
        # , conforming with the annotation standard for character count
        # P.S: here we can also create a paragraph mapping with word indices if desired.
        text_data = text_data.replace("\n\n", " <N> ")
        # create sentences to pass to the jsonline object
        sentences = [sent.split() for sent in text_data.split("\n")]
        tokens = text_data.split()

    return sentences, tokens

def convert_coref(
    from_file: str
    ) -> Tuple[Sentences, Tokens, CorefClusters]:
    """ given a .ann file, output the indices for the coreferent words

    Args:
        from_file (str): .ann file path
    Returns:
        Tuple[Sentences, Tokens, CorefClusters]:
            - sentences with tokens
            - tokens
            - a list of lists grouped by mention word index
    """

    grouped_mentions = get_reference_content(from_file)
    sentences, tokens = get_text_content(from_file)
    char_map = create_character_map(tokens)

    coref_clusters = []
    for mention_cluster in grouped_mentions:
        # ignore duplicated mentions
        tmp_cluster = set()
        for start, end in mention_cluster:
            ctw = char_to_word_index(char_map, start, end)
            if ctw:
                tmp_cluster.add(ctw)
        coref_clusters.append(list(tmp_cluster))

    # restore <N>-tag to newlines for readability
    for i, tok in enumerate(tokens):
        if tok == "<N>":
            tokens[i] = "\n"

    return sentences, tokens, coref_clusters
