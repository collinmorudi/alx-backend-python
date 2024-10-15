# Async Comprehension Project

## Overview
This project focuses on implementing asynchronous generators, async comprehensions, and measuring the runtime of parallel comprehensions using Python 3.7 on Ubuntu 18.04 LTS.

## Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreter: Python 3.7 on Ubuntu 18.04 LTS
- File format: All files must end with a new line and start with `#!/usr/bin/env python3`
- Coding style: pycodestyle (version 2.5.x)
- Documentation: Modules, functions, and coroutines must have detailed documentation

### Files and Structure
- **GitHub repository:** alx-backend-python
- **Directory:** 0x02-python_async_comprehension
- **Files:**
  - `0-async_generator.py`: Contains the `async_generator` coroutine.
  - `1-async_comprehension.py`: Contains the `async_comprehension` coroutine.
  - `2-measure_runtime.py`: Contains the `measure_runtime` coroutine.
  - `README.md`: This file.

## Tasks

### 0. Async Generator
- **File:** `0-async_generator.py`
- **Description:** This coroutine loops 10 times, asynchronously waits 1 second, and yields a random number between 0 and 10.
- **Example Usage:**
  ```python
  import asyncio

  async_generator = __import__('0-async_generator').async_generator

  async def print_yielded_values():
      result = []
      async for i in async_generator():
          result.append(i)
      print(result)

  asyncio.run(print_yielded_values())
  ```

### 1. Async Comprehensions
- **File:** `1-async_comprehension.py`
- **Description:** This coroutine collects 10 random numbers using an async comprehension over `async_generator` and returns the numbers.
- **Example Usage:**
  ```python
  import asyncio

  async_comprehension = __import__('1-async_comprehension').async_comprehension

  async def main():
      print(await async_comprehension())

  asyncio.run(main())
  ```

### 2. Run Time for Four Parallel Comprehensions
- **File:** `2-measure_runtime.py`
- **Description:** This coroutine executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.
- **Example Usage:**
  ```python
  import asyncio

  measure_runtime = __import__('2-measure_runtime').measure_runtime

  async def main():
      return await measure_runtime()

  print(asyncio.run(main()))
  ```

## Notes
- The total runtime for four parallel comprehensions is roughly 10 seconds because each comprehension takes approximately 10 seconds to complete, and they are executed in parallel.

## Contributing
Contributions are welcome. Ensure all code adheres to the pycodestyle (version 2.5.x) and includes detailed documentation for modules, functions, and coroutines.

## License
This project is licensed under the terms of the MIT License. See the LICENSE file for details.
