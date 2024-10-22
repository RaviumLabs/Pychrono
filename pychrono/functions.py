import time
import threading

# Delay function
def delay(milliseconds):
    """
    Pause the program for the specified number of milliseconds.
    
    Args:
        milliseconds (int): The number of milliseconds to delay.
    """
    if not isinstance(milliseconds, (int, float)):
        raise ValueError("Delay time must be an integer or float representing milliseconds.")
    time.sleep(milliseconds / 1000)

# Current time function
def current():
    """
    Get the current time in seconds since the epoch.
    
    Returns:
        float: The current time.
    """
    return time.time()

# Local function (raw)
def local_raw(seconds):
    """
    Convert seconds since the epoch to a struct_time in local time.
    
    Args:
        seconds (float): Time in seconds since the epoch.
    
    Returns:
        struct_time: A named tuple representing local time.
    """
    if not isinstance(seconds, (int, float)):
        raise ValueError("Seconds must be an integer or float.")
    return time.localtime(seconds)

# Local function (formatted)
def local(seconds):
    """
    Convert seconds since the epoch to a formatted string representing local time.
    
    Args:
        seconds (float): Time in seconds since the epoch.
    
    Returns:
        str: Local time in the format YYYY-MM-DD HH:MM:SS.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", local_raw(seconds))

# Monotonic function
def monotonic():
    """
    Get the current value of a monotonic clock, which cannot go backward.
    
    Returns:
        float: The value of a monotonic clock.
    """
    return time.monotonic()

# Countdown function
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