from typing import Callable, Any


def count_dec(func: Callable) -> Callable:
    count_dec.counter = 0

    def wrapped_func(*args, **kwargs) -> Any:
        count_dec.counter += 1
        print(count_dec.counter)
        func(*args, **kwargs)  # TODO: не забываем возвращать результат

    return wrapped_func


@count_dec
def some_func() -> None:
    print('Something is happening...\n')


for _ in range(3):
    some_func()
