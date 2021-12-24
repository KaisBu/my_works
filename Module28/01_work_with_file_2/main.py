from typing import Any


class File:
    """
    Класс Файл, аналог Open

    args and attrs:
        name: str Название файла
        mode: str Режим, может быть r, w, a иначе исключение
    """
    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self) -> Any:
        try:
            if self.mode == 'w' or self.mode == 'a' or self.mode == 'r':
                self.file = open(self.name, self.mode)
                return self.file
            else:
                raise ValueError
        except FileNotFoundError:
            self.file = open(self.name, 'w')
            return self.file
        except ValueError:
            print("Invalid mode: '{mode}'".format(mode=self.mode))

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.file:
            self.file.close()
        elif exc_type is ValueError:
            return True
        elif exc_type is AttributeError:
            return True
        elif exc_type is TypeError:
            return True


with File('01_work_with_file', 'a') as file:
    file.write('Hello world!\n')

with File('01_work_with_file', 'ngt') as file1:
    for string in file1:
        print(string)

with File('01_work_with_file1', 'ngt2') as file2:
    file2.write('Hello world!\n')




