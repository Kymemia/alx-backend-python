#!/usr/bin/env python3

"""
this program runs coroutines that each wait
for a random delay and returns them
in a list that's presented in ascending order
"""
import asyncio
from typing import List
import importlib
module = importlib.import_module("1-concurrent_coroutines")
task_wait_random = module.wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    method definition
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    for x in range(1, len(delays)):
        key = delays[x]
        y = x - 1
        while y >= 0 and key < delays[y]:
            delays[y + 1] = delays[y]
            y -= 1
        delays[y + 1] = key
    return delays
