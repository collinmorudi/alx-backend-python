# Python Async Functions

## Project Overview

This project is designed to demonstrate the use of asynchronous programming in Python, specifically focusing on the `async` and `await` syntax, the `asyncio` library, and the `random` module. The project is part of the ALX Backend Python course and is hosted in the `alx-backend-python` GitHub repository under the `0x01-python_async_function` directory.

### Learning Objectives

- Explain the `async` and `await` syntax.
- Execute an async program using `asyncio`.
- Run concurrent coroutines.
- Create `asyncio` tasks.
- Use the `random` module.

### Requirements

#### General

- A `README.md` file is mandatory at the root of the project folder.
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- All files must be executable.
- The length of files will be tested using `wc`.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Code should use the `pycodestyle` style (version 2.5.x).
- All functions and coroutines must be type-annotated.
- All modules should have documentation.
- All functions should have documentation.

### Tasks

#### 0. The Basics of Async

- **File:** `0-basic_async_syntax.py`
  - Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value of 10) and waits for a random delay between 0 and `max_delay` seconds before returning the delay.
  - Use the `random` module.

#### 1. Let's Execute Multiple Coroutines at the Same Time with Async

- **File:** `1-concurrent_coroutines.py`
  - Import `wait_random` from `0-basic_async_syntax.py`.
  - Write an async routine `wait_n` that takes two integer arguments `n` and `max_delay`, spawns `wait_random` `n` times with the specified `max_delay`, and returns a list of all delays in ascending order without using `sort()`.

#### 2. Measure the Runtime

- **File:** `2-measure_runtime.py`
  - Import `wait_n` from `1-concurrent_coroutines.py`.
  - Create a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns the average time per task.

#### 3. Tasks

- **File:** `3-tasks.py`
  - Import `wait_random` from `0-basic_async_syntax.py`.
  - Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

#### 4. Tasks

- **File:** `4-tasks.py`
  - Alter the code from `wait_n` to create a new function `task_wait_n` that uses `task_wait_random` instead of `wait_random`.

### Execution Examples

```bash
# Task 0
$./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769

# Task 1
$./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Task 2
$./2-main.py
1.759705400466919

# Task 3
$./3-main.py
<class '_asyncio.Task'>

# Task 4
$./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
```

### Documentation

Each module, function, and coroutine includes detailed documentation that explains its purpose. This documentation can be accessed using the following commands:

```bash
$ python3 -c 'print(__import__("my_module").__doc__)'
$ python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

### Style and Compliance

The project adheres to the `pycodestyle` style (version 2.5.x) and includes type annotations for all functions and coroutines. All files are executable, end with a new line, and start with the shebang `#!/usr/bin/env python3`.
