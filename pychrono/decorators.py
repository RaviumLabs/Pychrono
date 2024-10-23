import time
import signal
import threading
from typing import Callable, Tuple, TypeVar, Any

# Exception used in the timeout decorator
from .classes import TimeoutError

F = TypeVar('F', bound=Callable)

# Asynchronous decorator : approved
def asynchronous(func):
    """
    Decorator to run a function asynchronously using threading.
    
    Args:
        func (callable): The function to run asynchronously.
    
    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

# Cached decorator : approved
def cache(func):
    """
    A decorator that caches the results of a function based on its arguments.

    Args:
        func: The function to be decorated.

    Returns:
        The result of the function call, cached for future calls with the same arguments.
    """
    cache = {}

    def wrapper(*args, **kwargs):
        # Create a unique key for the cache based on arguments
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            # Return the cached result if it exists
            return cache[key]

        try:
            # Call the function and cache the result
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error occurred while executing {func.__name__}: {e}")
            raise  # Re-raise the exception after logging
    return wrapper

# Shedule decorator : approved
def schedule(seconds):
    """
    Decorator to schedule a function to run asynchronously after a specified delay.
    
    Args:
        seconds (int): The delay in milliseconds before running the function.
    
    Returns:
        callable: The decorated function that runs asynchronously after the delay.
    """
    if not isinstance(seconds, (int)) or seconds < 0:
        raise ValueError("Seconds must be a non-negative integer.")
    
    def deco_schedule(func):
        def wrapper(*args, **kwargs):
            def delayed_execution():
                time.sleep(seconds)
                func(*args, **kwargs)
            
            # Run the delayed execution in a separate thread
            thread = threading.Thread(target=delayed_execution)
            thread.start()
            return thread # Return the thread object to allow further management if needed
        return wrapper
    return deco_schedule

# Timer decorator : approved
def timer(func):
    """
    Decorator to measure the execution time of a function.
    
    Args:
        func (callable): The function to measure.
    
    Returns:
        callable: The decorated function that returns the execution time.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        total = time.time() - start
        return round(total, 5)
    return wrapper

# Repeat decorator : approved
def repeat(number):
    """
    Decorator to repeat a function a specified number of times.
    
    Args:
        number (int): The number of times to repeat the function.
    
    Returns:
        func: The decorated function.
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Repeat number must be a positive integer.")
    
    def deco_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(number):
                func(*args, **kwargs)
        return wrapper
    return deco_repeat

# Recurring decorator : approved
def recurring(interval):
    """
    Decorator to repeatedly execute a function at a specified interval.

    Args:
        interval (int): Time in seconds between each execution of the function.

    Raises:
        ValueError: If the interval is not a positive integer.

    Returns:
        function: A wrapped function that will run in a background thread at the specified interval.
    """

    # Validate that the interval is a positive integer
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError("Interval must be a positive float or integer representing seconds.")

    def deco_recurring(func):
        def wrapper(*args, **kwargs):
            def run_recurring():
                while True:
                    try:
                        func(*args, **kwargs) # Call the original function
                    except Exception as e:
                        print(f"An error occurred while executing the recurring task: {e}")
                    time.sleep(interval)

            # Start the recurring task in a new thread
            thread = threading.Thread(target=run_recurring)
            thread.daemon = True # Daemon thread will stop when the main program exits
            thread.start()

        # Return the wrapper, but don't call it immediately
        return wrapper
    return deco_recurring

# Throttle decorator : approved
def throttle(seconds: int):
    """
    A decorator that limits the rate of function calls to a specified interval.

    Args:
        seconds: The minimum time interval (in seconds) between calls to the function.

    Returns:
        The decorated function, rate-limited.

    Raises:
        TypeError: If the interval is not a positive integer.
    """
    if not isinstance(seconds, int) or seconds <= 0:
        raise TypeError("Throttle interval must be a positive integer.")

    def decorator(func: F) -> F:
        last_called = 0

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_called
            current_time = time.time()
            elapsed = current_time - last_called

            if elapsed < seconds:
                print(f"Function '{func.__name__}' is being throttled.")
                return  # Ignore calls made before the throttle period

            last_called = current_time
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Retry decorator : approved
def retry(max_attempts: int = 3, wait: int = 1):
    """
    A decorator that retries a function call if it raises an exception.

    Args:
        max_attempts: The maximum number of retry attempts.
        wait: The wait time (in seconds) between attempts.

    Returns:
        The result of the function call after successful execution.

    Raises:
        ValueError: If max_attempts is not a positive integer.
    """
    if not isinstance(max_attempts, int) or max_attempts <= 0:
        raise ValueError("max_attempts must be a positive integer.")
    if not isinstance(wait, (int, float)) or wait < 0:
        raise ValueError("wait time must be a non-negative number.")

    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}. Retrying...")
                    time.sleep(wait)
            raise RuntimeError(f"Function '{func.__name__}' failed after {max_attempts} attempts.")
        return wrapper
    return decorator

# Timeout decorator : approved
def timeout(seconds):
    """
    A decorator that raises a TimeoutException if the function takes too long to execute.

    Args:
        seconds: The maximum time (in seconds) allowed for the function execution.

    Returns:
        The result of the function call if it completes within the time limit.
    """
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("Function execution timed out.")

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds) # Set the alarm for the timeout duration
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0) # Disable the alarm
        return wrapper
    return decorator

# Validate decorator : approved
def validate(*expected_types: Tuple[type]):
    """
    A decorator that validates the types of arguments passed to a function.

    Args:
        expected_types: A tuple of valid types for the function's arguments.

    Returns:
        The result of the function call if all arguments are valid.

    Raises:
        TypeError: If any argument is not of the expected type.
    """
    def decorator(func: F) -> F:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Invalid argument type: {type(arg).__name__}. Expected: {expected_type.__name__}.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Timed cache decorator
def timed_cache(seconds: int):
    """
    A decorator that caches the result of a function for a specified duration.

    Args:
        seconds: The duration (in seconds) to cache the result.

    Returns:
        The result of the function call, either from cache or freshly computed.

    Raises:
        TypeError: If the duration is not a positive integer.
    """
    if not isinstance(seconds, int) or seconds <= 0:
        raise TypeError("Duration must be a positive integer.")

    def decorator(func: F) -> F:
        cache: Dict[Any, Any] = {}
        cache_time: Dict[Any, float] = {}

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = args  # Use args as cache key
            current_time = time.time()

            if key in cache and (current_time - cache_time[key] < seconds):
                print("Returning cached result.")
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result
            cache_time[key] = current_time
            return result
        return wrapper
    return decorator