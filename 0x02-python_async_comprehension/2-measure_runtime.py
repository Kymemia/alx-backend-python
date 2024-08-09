#!/usr/bin/env python3

"""
coroutine <measure_runtime> that executes <async_comrehension>
four times in parallel using <asyncio.gather>
measure_runtime measures the total runtime and returns it
"""
import time
import asyncio
from typing import List
import importlib
module = importlib.import_module("1-async_comprehension")
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """
    method definition
    """
    start_time = time.time()

    tasks = [
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension()),
            asyncio.create_task(async_comprehension())
            ]

    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
