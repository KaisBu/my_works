def single_list(some_list):
    if len(some_list) == 0:
        return some_list

    if isinstance(some_list[0], list):
        return single_list(some_list[0]) + single_list(some_list[1:])
    return some_list[:1] + single_list(some_list[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
nw_list = single_list(nice_list)
print(nw_list)
