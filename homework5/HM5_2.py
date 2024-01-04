# array = [1, 1, 2, 2, 3]

def second_smallest(array):
    array.sort()
    return array[1]

assert second_smallest([1, 1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1