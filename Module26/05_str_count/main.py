from collections.abc import Iterable
import os


def gen_fun(folder_path) -> Iterable[int]:
    for i_file in os.listdir(folder_path):
        new_path = os.path.join(folder_path, i_file)

        if new_path.endswith('.py'):
            with open(new_path, 'r', encoding='utf-8') as file:
                for strings in file:
                    if ('#' not in strings) and (len(strings.split()) != 0):
                        yield 1

        elif os.path.isdir(new_path):
            yield from gen_fun(folder_path=new_path)

    return


path = r'C:\Users\1\Desktop\skillbox_students\Кайс Бу-Хасан\python_basic\Module14'
string_count = 0

for i in gen_fun(folder_path=path):
    string_count += i

print(string_count)

# зачтено
