from collections.abc import Iterable
import os


def path_gen(folder, file_name: str) -> Iterable[os.path]:
    for i_file in os.listdir(folder):
        new_path = os.path.join(folder, i_file)
        yield new_path

        if i_file == file_name:
            return

        elif os.path.isdir(new_path):
            yield from path_gen(folder=new_path, file_name=file_name)

    return


path = r'C:\Users\1\Desktop\skillbox_students\Кайс Бу-Хасан\python_basic\Module14'
needed_file = 'main.py'

for file in path_gen(folder=path, file_name=needed_file):
    print(file)

# зачтено
