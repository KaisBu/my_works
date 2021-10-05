from typing import Callable
import functools


def debug(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        if args and kwargs:
            print('\nFunction is called {name}({args}, {kwargs})'.format(
                name=func.__name__,
                args=print_args(*args),
                kwargs=print_kwargs(**kwargs)
            ))
        elif args:
            print('\nFunction is called {name}({args})'.format(
                name=func.__name__,
                args=print_args(*args)
            ))
        elif kwargs:
            print('\nFunction is called {name}({kwargs})'.format(
                name=func.__name__,
                kwargs=print_kwargs(**kwargs)
            ))

        result = func(*args, **kwargs)

        print('{name} returned value {result}'.format(
            name=func.__name__,
            result=result
        ))

        print(result)
        return result

    return wrapped_func


@debug
def greeting(name: str, age=None) -> str:
    if age:
        return 'Wow, {name}! You are {age} years old, you are growing up fast!'.format(
            name=name,
            age=age
        )
    else:
        return 'Hello, {name}'.format(name=name)


def print_args(*args) -> str:
    some_lst = []
    for elem in args:
        some_lst.append(str(elem))
    return ', '.join(some_lst)


def print_kwargs(**kwargs) -> str:
    some_lst = []
    for key, value in kwargs.items():
        some_lst.append('{key}: {value}'.format(key=key, value=value))
    return ', '.join(some_lst)


greeting('Tom')
greeting('Michael', age=100)
greeting(name='Kate', age=16)
