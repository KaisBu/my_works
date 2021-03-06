from typing import Callable
import time


def sleep_dec(func: Callable) -> Callable:
    """decorator - delay 5 sec"""

    def wrapped_func(*args, **kwargs) -> None:
        time.sleep(5)
        return func(*args, **kwargs)

    return wrapped_func


@sleep_dec
def some_func() -> None:
    print('<Something is happening here...>')


some_func()

# зачтено
