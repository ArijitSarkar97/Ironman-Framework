import time
from functools import wraps
import logging

def retry_on_failure(retries=3, delay=1, exceptions=(Exception,)):
    """
    A decorator to automatically retry a test script or function upon failure.
    
    Args:
        retries (int): Number of times to retry the function before failing.
        delay (int): Delay in seconds between retries.
        exceptions (tuple): A tuple of exceptions to catch and retry on.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < retries:
                        logger.warning(
                            f"Execution failed with {str(e)}. "
                            f"Retrying ({attempt + 1}/{retries}) in {delay} seconds..."
                        )
                        time.sleep(delay)
                    else:
                        logger.error(f"Function {func.__name__} failed after {retries} retries.")
                        raise
        return wrapper
    return decorator
