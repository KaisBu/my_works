from datetime import datetime
import functools
from typing import Callable
import time


def log_with_format(_func: Callable = None, *, date_format: str = None) -> Callable:
    def log_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            cur_date = datetime.now()

            if date_format:
                print("- Запускается '{func_name}'. Дата и время запуска: {mo} {d} {y} - {h}:{mi}:{s}".format(
                    func_name=func.__name__,
                    mo=cur_date.month,
                    d=cur_date.day,
                    y=cur_date.year,
                    h=cur_date.hour,
                    mi=cur_date.minute,
                    s=cur_date.second
                ))
            else:
                print("- Запускается '{func_name}'. Дата и время запуска: {cur_date}".format(
                    func_name=func.__name__,
                    cur_date=cur_date
                ))
            start_time = time.time()
            result = func(*args, **kwargs)
            run_time = round(time.time() - start_time, 3)
            print("- Завершение '{func_name}', время работы = {run_time}s".format(
                func_name=func.__name__,
                run_time=run_time
            ))

            return result

        return wrapped
    if _func is None:
        return log_decorator
    else:
        return log_decorator(_func)


def log_methods(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith('__'):
                cur_method = getattr(cls, i_method)
                dec_method = decorator(cur_method)
                setattr(cls, i_method, dec_method)
        return cls
    return decorate


@log_methods(log_with_format(date_format="b d Y - H:M:S"))
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods(log_with_format(date_format="b d Y - H:M:S"))
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
