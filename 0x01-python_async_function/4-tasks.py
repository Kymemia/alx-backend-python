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

    delays.sort()
    return delays
