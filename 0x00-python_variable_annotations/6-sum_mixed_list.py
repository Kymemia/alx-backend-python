#!/usr/bin/env python3

"""
function that takes a list <mxd_lst>
of integers and floats
and returns their sum as float
"""
from typing import List, Any


def sum_mixed_list(mxd_lst: List[Any]) -> float:
    """
    method definition that takes a list
    of integers and floats and returns
    their sum as float
    """
    return sum(mxd_lst)
