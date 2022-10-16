from typing import Any, Dict, List, Set, Tuple

from coref_types import IndexRange, Markable, Sentences, Tokens


def make_jsonline(
    _id: str,
    sentences: Sentences,
    tokens: Tokens,
    clusters: List[List[Tuple[int, int]]]
    ) -> dict:
    """ create one item of a jsonline cluster

    Args:
        _id (str): document name/id
        tokens (List[str]): separate tokens (words)
        clusters (List[List[Tuple[int, int]]]): coreference clusters

    Returns:
        dict: jsonline-formatted object with coref information
    """
    return {
        "doc_key": _id,
        "sentences": sentences,
        "tokens": tokens,
        "clusters": clusters
    }

def mark_to_idx(markables: Markable, mark: str) -> IndexRange:
    """ convert a markable object to character start and end indices
    Args:
        mark (str): key to a markable object
    Returns:
        IndexRange: start/end character indices
    """
    return int(markables[mark]["start"]), int(markables[mark]["end"])

def create_character_map(tokens: Tokens) -> Dict[int, Dict[str, Any]]:
    """ map a character index to its token and word index
    Args:
        tokens (Tokens): space-separated tokens of the original text
    Returns:
        Dict[int, Dict[str, Any]]:
            mapping from a character index to the token text and its word index
    """
    char_map = {}
    char_idx = 0
    for i, tok in enumerate(tokens):
        char_map[char_idx] = {
            "token": tok,
            "word_index": i
        }
        incr = len(tok) + 1  # +1 to account for subsequent spaces
        if tok == "<N>":
            # only increment by 1 if we encounter a double newline
            incr = 1

        char_idx += incr
    return char_map

def expand_child(
    mapping: Dict[str, List[str]],
    visited: Set[str],
    entity: str,
    group: Set[str]
    ) -> None:
    if entity not in visited:
        group.add(entity)
        visited.add(entity)
        for child in mapping[entity]:
            expand_child(mapping, visited, child, group)


def char_to_word_index(char_map: Dict[int, Dict[str, int]], start, end) -> IndexRange:
    """ character index to word index

    Args:
        char_map (Dict[int, Dict[str, int]]): a conversion map from `create_character_map`
        chars (IndexRange): a tuple of two character indices

    Returns:
        IndexRange: a tuple of two word indices
    """
    index_range = [_i for _i in range(start, end + 1) if _i in char_map]
    span = [char_map[_j] for _j in index_range]
    if len(span) == 0:
        return None

    start_idx = span[0]["word_index"]
    end_idx = span[-1]["word_index"]

    return start_idx, end_idx
