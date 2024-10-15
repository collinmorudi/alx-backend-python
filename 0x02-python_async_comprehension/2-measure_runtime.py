#!/usr/bin/env python3
"""
This module contains a coroutine to measure the runtime
of executing multiple asynchronous comprehensions.
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


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using
    asyncio.gather, measures the total runtime and returns it.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()

    total_time = end_time - start_time
    return total_time


if __name__ == "__main__":
    async def main():
        runtime = await measure_runtime()
        print(runtime)

    asyncio.run(main())
