#!/usr/bin/env python3

"""
function to zoom in on an array
by reiterating every element
an exact number of times
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    method definition
    """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
