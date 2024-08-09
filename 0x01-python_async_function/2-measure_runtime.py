#!/usr/bin/env python3

"""
"""
import asyncio
import time
import importlib
module = importlib.import_module("1-concurrent_coroutines")
wait_n = module.wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    method definition
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
