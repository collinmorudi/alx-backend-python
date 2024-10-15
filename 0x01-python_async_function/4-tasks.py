#!/usr/bin/env python3
"""
This module contains a function to execute multiple coroutines
concurrently using asyncio.Tasks and return the list of delays.
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


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio Task for the wait_random coroutine
    with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with the specified max_delay.
    Returns the list of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


if __name__ == "__main__":
    import asyncio
    task_wait_n = __import__('4-tasks').task_wait_n

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
