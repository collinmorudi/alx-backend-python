#!/usr/bin/env python3
"""
This module contains an asynchronous generator
that yields random numbers between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields a random number between 0 and 10
    every 1 second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    import asyncio
    async_generator = __import__('0-async_generator').async_generator

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
