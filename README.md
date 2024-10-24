# Pychrono

[![Downloads](https://static.pepy.tech/badge/pychrono)](https://pepy.tech/project/pychrono)
[![PyPI version](https://badge.fury.io/py/pychrono.svg)](https://pypi.org/project/pychrono/)
[![Build Status](https://github.com/striatp/Pychrono/actions/workflows/main.yml/badge.svg)](https://github.com/striatp/Pychrono/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Pychrono** is a Python package designed for managing delays, scheduling tasks, timing functions, and more. It provides decorators for repeating tasks, scheduling actions, and running tasks asynchronously using threading. Pychrono simplifies time-related operations for both synchronous and asynchronous contexts. [View on PyPi](https://pypi.org/project/pychrono)

## Features
- **Delay execution** for a specific amount of time.
- **Get and format** the current system time.
- **Run tasks on a delay asynchronously**.
- **Repeat functions multiple times**.
- **Measure function execution time**.
- **Recurring task scheduling**.
- **Countdown timers**.
- **Retry functions** if they fail.
- **Limit function execution** rate.
- **Impose an execution timeout**.
- **Validate function arguments**.
- **Throttling function calls** to avoid frequent executions.
- **Calculate time differences** between two timestamps.
- **Uptime** tracking since program launch.
- **Program start time** retrieval.

## Changelog

### v1.1.0: Enhanced Functionality
This update focuses on enhancing existing functions and adding new ones for better usability and functionality.

**Added Functions:**
- `sleep_until(target_time)`: Pause execution until a specific time.
- `callback_timer(seconds, callback)`: Executes a callback function after a specified delay.
- `elapsed()`: Returns the program's elapsed time since the start.
- `repeat_for(duration, task)`: Repeats a task for a specified duration.
- `run_retry(seconds, task, retries)`: Attempts to run a task after a specified delay, retrying a given number of times if it fails.
- `schedule_at(delay, callback)`: Schedules a callback function to be called after a specified delay using threading.
- `time_diff(start, end)`: Calculate the difference in seconds between two timestamps.
- `uptime()`: Returns the system's uptime in seconds since the program was launched.
- `start_time()`: Returns the exact start time of the program in seconds since the epoch.

**Documentation:**
- Updated the docstrings and examples for all functions.

### v1.0.0: Public Release
This update focuses on enhancing and expanding the decorators.

**Added Decorators:**
- `@cache`: A decorator that caches the results of a function.
- `@throttle`: A decorator that limits how often a function is executed.
- `@retry`: A decorator that retries a function if it fails.
- `@timeout`: A decorator that imposes an execution time limit on a function.
- `@validate`: A decorator to validate the types of a function's arguments.
- `@timed_cache`: A decorator that caches results with an expiration period.

**Fixed Decorators:**
- `@schedule`: Improved for consistent execution timing.

---

## Installation

```bash
pip install pychrono
```

## Usage

### 1. Delays and Time Functions

#### Sleep Until
```python
import pychrono

# Sleep until a specific time (5 seconds from now)
target_time = pychrono.current() + 5
pychrono.sleep_until(target_time)
print("Woke up after 5 seconds!")
```

#### Callback Timer
```python
def task():
    print("Task executed after delay!")

# Schedule a task to run after 3 seconds
pychrono.callback_timer(3, task)
```

#### Elapsed Time
```python
# Get elapsed time since the program started
print(f"Elapsed Time: {pychrono.elapsed()} seconds")
```

#### Repeat For Duration
```python
def say_hello():
    print("Hello!")

# Repeat saying hello for 5 seconds
pychrono.repeat_for(5, say_hello)
```

#### Run Retry Function
```python
import random

def unstable_task():
    if random.random() < 0.5:
        raise Exception("Failed!")
    print("Task succeeded!")

# Retry the task up to 3 times with a 2-second delay between attempts
pychrono.run_retry(2, unstable_task, retries=3)
```

#### Schedule At
```python
def scheduled_task():
    print("This task was scheduled!")

# Schedule a task to run after 4 seconds
pychrono.schedule_at(4, scheduled_task)
```

### 2. Time Difference Calculation
```python
start = time.time()
pychrono.delay(2)  # Simulating a task that takes 2 seconds
end = time.time()

# Calculate the time difference
difference = pychrono.time_diff(start, end)
print(f"Time difference: {difference} seconds")
```

### 3. Uptime and Start Time
```python
# Get program uptime
print(f"Uptime: {pychrono.uptime()} seconds")

# Get program start time
print(f"Start Time: {pychrono.start_time()} seconds since the epoch")
```

### 4. Scheduling Functions

#### Schedule a Task
```python
# Schedule a task to run after 2 seconds
pychrono.schedule_at(2, say_hello)  # Prints "Hello!" after 2 seconds
```

### 5. Decorators

#### Repeat Function Execution
```python
@pychrono.repeat(3)
def greet():
    print("Hello!")

greet()  # This will print "Hello!" three times
```

#### Cache Function Results
```python
@pychrono.cache
def heavy_computation(x):
    print(f"Computing for {x}")
    return x * x

print(heavy_computation(2))  # Outputs: 4 and caches the result
print(heavy_computation(2))  # Uses cached result
```

#### Time a Function's Execution
```python
@pychrono.timer
def long_task():
    for _ in range(1000000):
        pass

# Print the time taken to run the function
long_task()
```

#### Limit Function Execution Rate (`@throttle`)
```python
@pychrono.throttle(2)  # Allow execution only every 2 seconds
def greet_throttled():
    print("Throttled Hello!")

greet_throttled()  # Prints immediately
greet_throttled()  # Throttled, won't print if called within 2 seconds
```

#### Retry Function Execution (`@retry`)
```python
@pychrono.retry(max_attempts=3, wait=2)
def unstable_task():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    print("Success!")

unstable_task()  # Retries up to 3 times with a 2-second wait between attempts
```

#### Validate Function Arguments (`@validate`)
```python
@pychrono.validate(int, float)
def add(a, b):
    return a + b

print(add(3, 4.5))  # Valid input, prints: 7.5
# print(add(3, 'four'))  # Raises TypeError
```

#### Cache Results with Expiration (`@timed_cache`)
```python
@pychrono.timed_cache(5)  # Cache results for 5 seconds
def expensive_function(x):
    print(f"Expensive calculation for {x}")
    return x * 2

print(expensive_function(3))  # Performs calculation
print(expensive_function(3))  # Uses cached result if called within 5 seconds
```

#### Execute a Function Repeatedly (`@recurring`)
```python
@pychrono.recurring(2)  # Run every 2 seconds
def print_message():
    print("This message will print every 2 seconds.")

# Start the recurring task
print_message()

# Prevent the main thread from exiting immediately
while True:
    time.sleep(1)
```

#### Schedule a Task with Delay (`@schedule`)
```python
@pychrono.schedule(2)  # Delay for 2 seconds
def say_hello():
    print("Hello after 2 seconds!")

say_hello()  # Prints "Hello" after 2 seconds without blocking
```

#### Run a Function Asynchronously (`@asynchronous`)
```python
@pychrono.asynchronous
def task():
    print("Running asynchronously!")

task()  # Runs in a separate thread
```

## More Features Coming Soon!
Stay tuned for more functionalities such as:
- Enhanced threading control and task management.
- Time zone support for easier global time handling.
- And much more!

Feel free to contribute to the project, raise issues, or suggest features by visiting our [GitHub repository](https://github.com/striatp/Pychrono).

### License
Pychrono is licensed under the MIT License.