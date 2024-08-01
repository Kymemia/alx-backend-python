#!/usr/bin/env python3

"""
function to zoom in on an array
by reiterating every element
an exact number of times
"""
from typing import Tuple, List, Union


def zoom_array(lst: Union[Tuple, List], factor: int = 2) -> List:
    """
    method definition
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
