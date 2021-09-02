import os


def path_gen(folder, file_name: str) -> os.path:

    for i_file in os.listdir(folder):
        new_path = os.path.join(folder, i_file)
        yield new_path

        if i_file == file_name:
            yield None

        if os.path.isdir(new_path):
            for files in path_gen(folder=new_path, file_name=file_name):
                if files:
                    yield files
                else:
                    return


path = os.path.abspath(os.path.join(os.path.sep, 'Users', 'Кайс', 'PycharmProjects',
                                    'python_basic', 'Module19'))
needed_file = 'main.py'

for file in path_gen(folder=path, file_name=needed_file):
    print(file)




