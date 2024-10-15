#!/usr/bin/env python3
"""
This module contains an asynchronous comprehension
that collects 10 random numbers from an async generator.
"""


import asyncio
import random
from typing import List


async def async_generator() -> float:
    """
    Asynchronously yields a random number between 0 and 10
    every 1 second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator and returns the list of numbers.
    """
    return [i async for i in async_generator()]
