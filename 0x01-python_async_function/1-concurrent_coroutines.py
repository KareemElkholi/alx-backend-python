#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
from typing import List
from asyncio import create_task, as_completed
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return the list of all the delays"""
    tasks = [create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in as_completed(tasks)]
