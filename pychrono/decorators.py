import time
import threading

# Asynchronous decorator
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

# Shedule decorator
def schedule(milliseconds):
    """
    Decorator to schedule a function to run asynchronously after a specified delay.
    
    Args:
        milliseconds (int): The delay in milliseconds before running the function.
    
    Returns:
        callable: The decorated function that runs asynchronously after the delay.
    """
    if not isinstance(milliseconds, (int, float)) or milliseconds < 0:
        raise ValueError("Milliseconds must be a non-negative integer or float.")
    
    def deco_schedule(func):
        def wrapper(*args, **kwargs):
            def delayed_execution():
                time.sleep(milliseconds / 1000)
                func(*args, **kwargs)
            
            # Run the delayed execution in a separate thread
            thread = threading.Thread(target=delayed_execution)
            thread.start()
            return thread  # Return the thread object to allow further management if needed
        
        return wrapper
    
    return deco_schedule

# Timer decorator
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
        print(f"Execution time: {total:.4f} seconds")
        return result
    return wrapper

# Repeat decorator
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