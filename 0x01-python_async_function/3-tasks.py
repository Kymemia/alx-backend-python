#!/usr/bin/env python3

"""
function that takes an integer, max_delay, and returns a asyncio.Task
"""
import asyncio
import importlib
module = importlib.import_module("0-basic_async_syntax")
wait_random = module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    method definiction
    """
    return asyncio.create_task(wait_random(max_delay))
