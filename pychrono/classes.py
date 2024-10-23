import time

# Class to initialize a timer
class Timer:
    """
    A simple timer class that supports start, pause, resume, and elapsed time functionalities.
    """

    # Initializing
    def __init__(self):
        """Initialize the timer with no start time and no paused state."""
        self.start_time = None
        self.paused_time = None
        self.total_pause_duration = 0

    # Method to start the timer
    def start(self):
        """Start the timer."""
        if self.start_time is None:
            self.start_time = time.time()
        else:
            raise RuntimeError("Timer is already running.")

    # Method to pause the timer
    def pause(self):
        """Pause the timer."""
        if self.start_time is None:
            raise RuntimeError("Timer has not been started yet.")
        if self.paused_time is None:
            self.paused_time = time.time()

    # Method to resume the timer
    def resume(self):
        """Resume the timer after it has been paused."""
        if self.paused_time is not None:
            self.total_pause_duration += time.time() - self.paused_time
            self.paused_time = None
        else:
            raise RuntimeError("Timer is not paused.")

    # Method to calculate the elapsed time
    def elapsed(self):
        """
        Calculate the elapsed time in seconds.
        
        Returns:
            float: The total elapsed time in seconds.
        """
        if self.start_time is None:
            raise RuntimeError("Timer has not been started yet.")
        if self.paused_time is not None:
            return self.paused_time - self.start_time - self.total_pause_duration
        return time.time() - self.start_time - self.total_pause_duration

    # Method to reset the timer
    def reset(self):
        """Reset the timer to its initial state."""
        self.start_time = None
        self.paused_time = None
        self.total_pause_duration = 0

    # Default string value of the instance
    def __str__(self):
        """
        Return a string representation of the elapsed time.
        
        Returns:
            str: Elapsed time in seconds, rounded to 3 decimal places.
        """
        return f"{self.elapsed()}"

# Class for raised timeout exception
class TimeoutError(Exception):
    """Custom exception for timeout handling."""
    pass