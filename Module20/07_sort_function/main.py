def sorting_function(some_tuple):
    for element in some_tuple:
        if not isinstance(element, int):
            return some_tuple
    return sorted(some_tuple)


new_tuple = (6, 9, 1, 0, 52, 0.251, 5)
print(sorting_function(new_tuple))
