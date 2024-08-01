#!/usr/bin/env python3

"""
adding type notations to the function
"""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    method definition
    """
    if key in dct:
        return dct[key]
    else:
        return default
