from typing import Dict, List, Tuple

Markable = Dict[str, Dict[str, str]]
MarkableReference = Tuple[str, str]
IndexRange = Tuple[int, int]
MarkableGroup = Tuple[IndexRange, IndexRange]
CorefClusters = List[List[IndexRange]]
Tokens = List[str]
Sentences = List[Tokens]
