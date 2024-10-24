# Pychrono

[![Downloads](https://static.pepy.tech/badge/pychrono)](https://pepy.tech/project/pychrono)
[![PyPI version](https://badge.fury.io/py/pychrono.svg)](https://pypi.org/project/pychrono/)
[![Build Status](https://github.com/striatp/Pychrono/actions/workflows/main.yml/badge.svg)](https://github.com/striatp/Pychrono/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Pychrono** is a Python package designed for managing delays, scheduling tasks, timing functions, and more. It provides decorators for repeating tasks, scheduling actions, and running tasks asynchronously using threading. Pychrono simplifies time-related operations for both synchronous and asynchronous contexts. [View on PyPi](https/pypi.org/project/pychrono)

## Features
- **Delay execution** for a specific amount of time.
- **Get and format** the current system time.
- **Run tasks on a delay asynchronously**.
- **Repeat functions multiple times**.
- **Measure function execution time**.
- **Recurring task scheduling**.
- **Countdown timers**.
- **Cache function results** with expiration.
- **Retry functions** if they fail.
- **Limit function execution** rate.
- **Impose an execution timeout**.
- **Validate function arguments**.
- **Throttle function calls** to avoid frequent executions.

## Changelog

For the next update, we are aiming to rework and enhance our existing functions and add new ones.

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

**Documentation:**
- Updated the docstrings and examples of all decorators.

### v0.1.2
- Added a `@recurring` decorator to always execute a function at specified intervals.
- Added a `.countdown(seconds, callback)` method to execute a function after a countdown.

### v0.1.1
- `.elapsed` and `Timer` (`__str__`) now output a non-rounded string without "seconds" to avoid type casting issues.

---

## Installation

```bash
pip install pychrono
```

## Usage

### 1. Delays and Time Functions

#### Delay Execution
```python
import pychrono

# Delay execution for 1000 milliseconds (1 second)
pychrono.delay(1000)
```

#### Get Current Time
```python
# Get the current time in seconds since the epoch
current_time = pychrono.current()
print(f"Current time: {current_time}")
```

#### Convert Time to Local String
```python
# Convert time to a readable local time string
seconds = pychrono.current()
formatted_time = pychrono.local(seconds)
print(f"Local time: {formatted_time}")
```

#### Start a Countdown on a Function
```python
def times_up():
    print("Time's up!")

# Start a countdown from 5 seconds
pychrono.countdown(5, times_up)
```

### 2. Decorators

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
@pychrono.schedule(2000)  # Delay for 2000 milliseconds (2 seconds)
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

### 3. Timer Class

The `Timer` class allows you to start, pause, resume, and get the elapsed time. Printing the timer object directly will output the seconds elapsed.

#### Start, Pause, and Resume Timer
```python
# Create a timer instance
timer = pychrono.Timer()

# Start the timer
timer.start()

# Perform some task
pychrono.delay(2000)  # Delay for 2 seconds

# Get the elapsed time
print(f"Elapsed: {timer}")  # Prints elapsed time in seconds (e.g., 2.0)

# Pause the timer
timer.pause()

# Resume the timer
timer.resume()

# Get updated elapsed time
pychrono.delay(1000)  # Delay for 1 more second
print(f"Updated Elapsed: {timer}")  # Prints updated elapsed time (e.g., 3.0)
```

## More Features Coming Soon!
Stay tuned for more functionalities such as:
- Enhanced threading control and task management.
- Time zone support for easier global time handling.
- And much more!

Feel free to contribute to the project, raise issues, or suggest features by visiting our [GitHub repository](https://github.com/striatp/Pychrono).

### License
Pychrono is licensed under the MIT License.

---