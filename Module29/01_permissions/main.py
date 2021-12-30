import functools
from typing import Callable


user_permissions = ['admin']


def check_permission(permission: str) -> Callable:
    def permission_dec(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if permission == 'admin':
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                    func_name=func.__name__
                ))
        return wrapped
    return permission_dec


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

