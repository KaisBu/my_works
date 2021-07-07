import os


def folders_weight(path):
    if os.path.isfile(path):
        return os.path.getsize(path)

    for element in os.listdir(path):
        result = folders_weight(os.path.join(path, element))
        if result:
            if isinstance(result, int):
                files_list.append(result)


files_list = []
folders_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
folders_weight(folders_path)

print('Directory size (Kb):', sum(files_list) / 1000)
print('Number of subdirectories:', len(os.listdir(folders_path)))
print('Number of files:', len(files_list))
