from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(*args, **kwargs):
        print('Переданные арги и кварги в декоратор:', args, kwargs)
        return decorator
    return decorate


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:

    @functools.wraps(func)
    def wrapper(*args1, **kwargs1):
        return func(*args1, **kwargs1)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
