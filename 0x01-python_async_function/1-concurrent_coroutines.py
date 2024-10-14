#!/usr/bin/env python3
"""
This module contains a coroutine that executes multiple
coroutines concurrently and returns a list of delays.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive) seconds and
    eventually returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times with the specified max_delay.
    Returns the list of all delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


# Example usage
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
