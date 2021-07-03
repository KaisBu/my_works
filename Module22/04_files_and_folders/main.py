import os


def folders_weight(path, summ_list=[]):
    if os.path.isfile(path):
        return os.path.getsize(path)

    for element in os.listdir(path):
        result = folders_weight(os.path.join(path, element))
        if result:
            summ_list.append(result)

    print(sum(summ_list))



folders_weight(os.path.abspath(os.path.join('..', '..', 'Module22')))

