#!/usr/bin/env python3
"""0. The basics of async"""
from asyncio import sleep
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    delay = random() * max_delay
    await sleep(delay)
    return delay
