from typing import Callable, Any
import datetime
import os
import functools
import time


def logging(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(0.5)
        path = os.path.abspath('log.txt')
        print('\nFunction name: {name}'.format(name=func.__name__))
        print('Documentation: {docs}'.format(docs=func.__doc__))

        try:
            func(*args, **kwargs)
        except TypeError:
            with open(path, 'a') as file:
                error = 'TypeError, time: {time}\n'.format(
                    time=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
                file.write(error)
        except FileNotFoundError:
            with open(path, 'a') as file:
                error = 'FileNotFoundError, time: {time}\n'.format(
                    time=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
                file.write(error)
        except ZeroDivisionError:
            with open(path, 'a') as file:
                error = 'ZeroDivisionError, time: {time}\n'.format(
                    time=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
                file.write(error)
        except IndexError:
            with open(path, 'a') as file:
                error = 'IndexError, time: {time}\n'.format(
                    time=datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
                file.write(error)

    return wrapped_func


@logging
def worked_func() -> None:
    """This function is doing something"""
    print('<Something is happening here...>')


@logging
def type_error():
    """Function calls TypeError"""
    raise TypeError


@logging
def file_not_found_error():
    """Function calls FileNotFoundError"""
    raise FileNotFoundError


@logging
def zero_division_error():
    """Function calls ZeroDivisionError"""
    raise ZeroDivisionError


@logging
def index_error():
    """Function calls IndexError"""
    raise IndexError


worked_func()
type_error()
file_not_found_error()
zero_division_error()
index_error()
