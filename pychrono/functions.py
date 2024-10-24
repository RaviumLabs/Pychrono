import time
import threading

# Get the time when the program started
program_start_time = time.time()

# Delay function : approved
def delay(seconds):
    """
    Pause the program for the specified number of seconds.
    
    Args:
        seconds (int): The number of seconds to delay.
    """
    if not isinstance(seconds, (int, float)):
        raise ValueError("Delay time must be an integer or float representing seconds.")
    time.sleep(seconds)

# Current time function : approved
def current():
    """
    Get the current time in seconds since the epoch.
    
    Returns:
        float: The current time.
    """
    return time.time()

# Local function (raw) : approved
def local_raw(seconds):
    """
    Convert seconds since the epoch to a struct_time in local time.
    
    Args:
        seconds (float): Time in seconds since the epoch.
    
    Returns:
        struct_time: A named tuple representing local time.
    """
    if not isinstance(seconds, int):
        raise ValueError("Seconds must be a positive integer.")
    return time.localtime(seconds)

# Local function (formatted) : approved
def local(seconds):
    """
    Convert seconds since the epoch to a formatted string representing local time.
    
    Args:
        seconds (float): Time in seconds since the epoch.
    
    Returns:
        str: Local time in the format YYYY-MM-DD HH:MM:SS.
    """
    if not isinstance(seconds, int):
        raise ValueError("Seconds must be a positive integer.")
    return time.strftime("%Y-%m-%d %H:%M:%S", local_raw(seconds))

# Monotonic function : approved
def monotonic():
    """
    Get the current value of a monotonic clock, which cannot go backward.
    
    Returns:
        float: The value of a monotonic clock.
    """
    return time.monotonic()

# Countdown function : approved
def countdown(seconds, callback):
    """
    Starts a countdown timer and calls the callback function when the time is up.

    Args:
        seconds (int): Number of seconds to countdown.
        callback (function): Function to be called when the countdown finishes.

    Raises:
        ValueError: If 'seconds' is not a positive integer.
    """

    # Validate input
    if not isinstance(seconds, int) or seconds <= 0:
        raise ValueError("The 'seconds' parameter must be a positive integer.")

    def countdown_timer():
        """
        Inner function that runs the countdown in a separate thread.
        It decrements the seconds and calls the callback when done.
        """
        nonlocal seconds  # Use 'nonlocal' to modify the outer 'seconds' variable
        while seconds > 0:
            time.sleep(1)  # Sleep for 1 second
            seconds -= 1

        try:
            callback()  # Call the callback function when the countdown finishes
        except Exception as e:
            print(f"Error occurred while executing the callback: {e}")

    # Start the countdown in a new thread
    thread = threading.Thread(target=countdown_timer)
    thread.start()

# Slee until function : approved
def sleep_until(target_time):
    """
    Pause execution until the specified target time (in seconds since the epoch).

    Args:
        target_time (float): The target time in seconds since the epoch.
    
    Raises:
        ValueError: If target_time is not a float or if it is in the past.
    """
    if not isinstance(target_time, (int, float)):
        raise ValueError("Target time must be an integer or float representing seconds since the epoch.")
    current_time = time.time()
    if target_time <= current_time:
        raise ValueError("Target time must be in the future.")
    delay(target_time - current_time)

# Callback timer function : approved
def callback_timer(seconds, callback):
    """
    Executes the callback function after a specified delay.

    Args:
        seconds (int | float): The number of seconds to wait before executing the callback.
        callback (function): The function to execute after the delay.

    Raises:
        ValueError: If seconds is not a positive number.
        TypeError: If callback is not callable.
    """
    if not isinstance(seconds, (int, float)) or seconds <= 0:
        raise ValueError("Seconds must be a positive integer or float.")
    if not callable(callback):
        raise TypeError("Callback must be a callable function.")
    delay(seconds)
    callback()

# Elapsed function : approved
def elapsed():
    """
    Returns the program's start time in a human-readable format.

    Returns:
        str: The program's start time in seconds.
    """
    elapsed_time = time.time() - program_start_time
    return int(elapsed_time)

# Repeat for function : approved
def repeat_for(duration, task):
    """
    Repeats a given task for a specified duration.

    Args:
        task (function): The function to repeat.
        duration (int | float): The duration in seconds for which to repeat the task.

    Raises:
        ValueError: If duration is not a positive number or if task is not callable.
    """
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError("Duration must be a positive number.")
    if not callable(task):
        raise TypeError("Task must be callable.")
    end_time = time.time() + duration
    while time.time() < end_time:
        task()

# Run retry function
def run_retry(seconds, task, retries):
    """
    Attempts to run a task after a specified delay, retrying a given number of times if it fails.

    Args:
        task (function): The function to execute.
        seconds (int | float): The number of seconds to wait before attempting the task.
        retries (int): The number of retry attempts.

    Raises:
        ValueError: If seconds is not a positive number or if retries is not a positive integer.
        TypeError: If task is not callable.
    """
    if not isinstance(seconds, (int, float)) or seconds <= 0:
        raise ValueError("Seconds must be a positive number.")
    if not isinstance(retries, int) or retries <= 0:
        raise ValueError("Retries must be a positive integer.")
    if not callable(task):
        raise TypeError("Task must be callable.")
    for attempt in range(retries):
        try:
            delay(seconds)
            return task()  # Execute the task
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    print("All attempts failed.")

# Schedule at function : approved
def schedule_at(delay, callback):
    """
    Schedules a callback function to be called after a specified delay using threading.

    Args:
        delay (float): The delay in seconds before the callback is executed.
        callback (function): The function to be called after the delay.

    Raises:
        ValueError: If delay is not a number representing seconds.
    """
    if not isinstance(delay, (int, float)):
        raise ValueError("Delay must be a number representing seconds.")

    def delayed_execution():
        """Inner function that waits for the delay and then executes the callback."""
        time.sleep(delay)  # Blocking sleep
        callback()

    # Create and start a new thread
    thread = threading.Thread(target=delayed_execution)
    thread.start()

# Time difference function : approved
def time_diff(start, end):
    """
    Calculate the difference in seconds between two times.

    Args:
        start (float): The start time in seconds since the epoch.
        end (float): The end time in seconds since the epoch.

    Returns:
        float: The difference in seconds.

    Raises:
        ValueError: If either start or end is not a number.
    """
    if not all(isinstance(t, (int, float)) for t in [start, end]):
        raise ValueError("Both start and end must be numbers representing seconds.")
    return end - start

# Uptime function : approved
def uptime():
    """
    Returns the system's uptime in seconds since the program was launched.

    Returns:
        float: The uptime in seconds since the program started.
    """
    return time.monotonic()

# Start time function : approved
def start_time():
    """
    Returns the exact start time of the program in seconds since the epoch.

    Returns:
        float: The start time of the program.
    """
    return program_start_time