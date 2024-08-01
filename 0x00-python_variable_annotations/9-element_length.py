#!/usr/bin/env python3

"""
Annotation of the function's parameters
and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """method definition that iterates through strings/lists
    and returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
