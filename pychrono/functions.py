import time

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