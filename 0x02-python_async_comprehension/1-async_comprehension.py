#!/usr/bin/env python3

"""
this is a coroutine named, async_comprehension
that takes no arguments
it collects 10 random numbers using an async comprehensing
over <async_generator>, then returns said 10 random numbers
"""
import asyncio
from typing import List
import importlib
module = importlib.import_module("0-async_generator")
async_generator = module.async_generator


async def async_comprehension() -> List[float]:
    """
    method definition
    """
    return [number async for number in async_generator()]
