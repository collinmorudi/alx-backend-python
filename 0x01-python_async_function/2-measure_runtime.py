#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of
executing a coroutine multiple times.
"""


import asyncio
import time
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


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per coroutine call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
