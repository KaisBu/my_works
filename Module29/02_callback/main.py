from typing import Callable, Any
import functools


def callback(sym: str) -> Callable:
    def callback_1(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            if sym == '//':
                return func(*args, *kwargs)
            else:
                return None
        return wrapped
    return callback_1


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {
    '//': example
}

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

