#!/usr/bin/env python3

"""
coroutine that takes in an integer argument:
(max_delay, default alue == 10), named (wait_random)
Waits for a random delay between 0 and max_delay(included && float value)
seconds and returns it
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    method definition
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
