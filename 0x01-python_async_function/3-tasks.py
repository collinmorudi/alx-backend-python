#!/usr/bin/env python3
"""
This module contains a function to create an asyncio Task
for a given coroutine.
"""


import asyncio
import random


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


if __name__ == "__main__":
    import asyncio
    task_wait_random = __import__('3-tasks').task_wait_random

    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
