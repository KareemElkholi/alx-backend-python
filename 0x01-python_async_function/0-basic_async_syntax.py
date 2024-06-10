#!/usr/bin/env python3
"""0. The basics of async"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
