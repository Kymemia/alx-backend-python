#!/usr/bin/env python3

"""
function takes a string k and an int OR float v
as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v,
and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes string (k) and int/float (v) as args. Returns tuple
    First element => string, k
    Second element => square of int/float (v)
    """
    squared = v ** 2
    if squared % 1 == 0:
        return (k, int(squared))
    else:
        return (k, squared)
