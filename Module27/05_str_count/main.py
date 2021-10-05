from typing import Callable, Any


def count_dec(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        wrapped_func.counter += 1
        print('Counter:', wrapped_func.counter)
        return func(*args, **kwargs)

    wrapped_func.counter = 0
    return wrapped_func


@count_dec
def some_func() -> None:
    print('Something is happening...\n')


for _ in range(3):
    some_func()
