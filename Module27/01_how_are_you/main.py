from typing import Callable


def decorator(func: Callable) -> Callable:
    """Annoying decorator"""
    def wrapped_func(*args, **kwargs) -> None:
        greeting = input('Hi! How are you? ')
        print('And mine is not very good! Okay, keep your function')
        func(*args, **kwargs)

    return wrapped_func


@decorator
def some_func() -> None:
    print('<Something is happening here...>')


some_func()
