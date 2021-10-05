from typing import Callable


def decorator(func: Callable) -> Callable:
    """Annoying decorator"""

    def wrapped_func(*args, **kwargs) -> str:
        greeting = input('Hi! How are you? ')
        print('And mine is not very good! Okay, keep your function')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@decorator
def some_func() -> str:
    result = '<Something is happening here...>'
    return result


print(some_func())

# зачтено
