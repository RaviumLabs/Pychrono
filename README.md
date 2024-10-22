# Pychrono

**Pychrono** is a Python package designed for managing delays, scheduling tasks, timing functions, and more. It provides decorators for repeating tasks, scheduling actions, and running tasks asynchronously using threading. Pychrono simplifies time-related operations for both synchronous and asynchronous contexts.

## Features
- Delay execution for a specific amount of time.
- Get the current system time and format it.
- Run tasks on a delay asynchronously.
- Repeat functions multiple times.
- Measure function execution time.
- Use a robust `Timer` class with start, pause, resume, and elapsed time tracking.

## Changlogs 0.1.1
- `.elapsed` and `Timer` (\_\_str\_\_) now output a non-rounded string without "seconds" that led to type casting issues.

---

## Installation

```bash
pip install pychrono
```
## Usage

### 1. Delays and Time Functions
Delay Execution
```python
import pychrono

# Delay execution for 1000 milliseconds (1 second)
pychrono.delay(1000)
```
Get Current Time
```python
# Get the current time in seconds since the epoch
current_time = pychrono.current()
print(f"Current time: {current_time}")
```
Convert Time to Local String
```python
# Convert time to a readable local time string
seconds = pychrono.current()
formatted_time = pychrono.local(seconds)
print(f"Local time: {formatted_time}")
```

### 2. Decorators
Repeat Function Execution
```python
@pychrono.repeat(3)
def greet():
    print("Hello!")

greet()  # This will print "Hello!" three times
```
Time a Function's Execution
```python
@pychrono.timer
def long_task():
    for _ in range(1000000):
        pass

# Print the time taken to run the function
long_task()
```
Asynchronous Scheduling with Delay
```python
@pychrono.schedule(2000)  # Delay for 2000 milliseconds (2 seconds)
def say_hello():
    print("Hello after 2 seconds!")

say_hello()  # Will print "Hello" after 2 seconds without blocking
```
Run a Function Asynchronously
```python
@pychrono.asynchronous
def task():
    print("Running asynchronously!")

task()  # Runs in a separate thread
```

### 3. Timer Class
The Timer class allows you to start, pause, resume, and get the elapsed time. Printing the timer object directly will output the seconds elapsed.

Start, Pause, and Resume Timer
```python
# Create a timer instance
timer = pychrono.Timer()

# Start the timer
timer.start()

# Perform some task
time.sleep(2)

# Get the elapsed time
print(f"Elapsed: {timer}")  # Prints elapsed time in seconds (e.g., 2.0)

# Pause the timer
timer.pause()

# Resume the timer
timer.resume()

# Get updated elapsed time
time.sleep(1)
print(f"Updated Elapsed: {timer}")  # Prints updated elapsed time (e.g., 3.0)
```
## More Features Coming Soon!
Stay tuned for more functionalities such as:

- Recurring scheduled tasks.
- Enhanced threading control and task management.
- Time zone support for easier global time handling.
- And much more!

Feel free to contribute to the project, raise issues, or suggest features by visiting our [GitHub repository](https://github.com/striatp/Pychrono).

### License
Pychrono is licensed under the MIT License.