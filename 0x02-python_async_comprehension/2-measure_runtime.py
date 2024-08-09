#!/usr/bin/env python3

"""
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

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    end_time = time.time()
    return end_time - start_time
