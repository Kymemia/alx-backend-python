#!/usr/bin/env python3

"""
this is a coroutine named async_generator
it loops 10 times, each time asynchornously waiting 1 second,
then yields a andom number between 0 and 10
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    method definition
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
