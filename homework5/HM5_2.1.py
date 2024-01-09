def second_smallest(array):
    lst = list(set(array))
    lst.sort()
    return lst[1]

assert second_smallest([1, 1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1