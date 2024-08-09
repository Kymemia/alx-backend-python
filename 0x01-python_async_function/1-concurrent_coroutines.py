#!/usr/bin/env python3

"""
async routines named, wait_n
takes in 2 int arguments in this order:
    n && max_delay
spawn wait_random (n) times with the specified max_delay
wait_n returns the list of all delays (float values) in asc. order
"""
import asyncio
from typing import List
import importlib
module = importlib.import_module("0-basic_async_syntax")
wait_random = module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    method definition
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    for x in range(1, len(delays)):
        key = delays[x]
        y = x - 1
        while y >= 0 and key < delays[y]:
            delays[y + 1] = delays[y]
            y -= 1
        delays[y + 1] = key

    return delays
