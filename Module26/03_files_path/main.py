import os


def path_gen(folder, file_name):

    for element in os.listdir(folder):
        path = os.path.join(folder, element)

        if os.path.isfile(path):
            print(path)
            if element == file_name:
                break
            return path
        elif os.path.isdir(path):
            path_gen(path, file_name)


path = os.path.abspath(os.path.join(os.path.sep, 'Users', 'Испытатель'))
needed_file = 'main.py'

path_gen(path, needed_file)

