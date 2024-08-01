#!/usr/bin/env python3

"""
function takes a float <multiplier> as arg
and returns a function that multiplies
a float by <multiplier>
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a given float
    by a multiplier

    args: multiplier (float)
    return: function that multiplies
            a float by multiplier
    """
    def actual_product(x: float) -> float:
        """
        Calls the `multiplier` arg and multiplies it by x
        """
        return multiplier * x

    return actual_product
