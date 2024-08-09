#!/usr/bin/env python3

"""
measure_time function with integers, n and max_delay as args
that measures the total execution time for wait_n(n, max_delay)
Returns total_time / n (float)
"""
import asyncio
import time
import importlib
module = importlib.import_module("1-concurrent_coroutines")
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    method definition
    """
    async def _measure_time(n: int, max_delay: int) -> float:
        start_time = time.time()
        delay = await wait_n(n, max_delay)
        end_time = time.time()
        total_time = end_time - start_time
        return total_time / n

    return asyncio.run(_measure_time(n, max_delay))
