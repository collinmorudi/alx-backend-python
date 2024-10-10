#!/usr/bin/env python3
"""9-element_length"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotated function that takes an iterable of sequences and returns
    a list of tuples.
    Each tuple contains a sequence from the iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
