def join_ints(my_list):
    counter = 0
    for i in my_list:
        if isinstance(i, int):
            counter = counter * 10 + i

    print(counter)

    return counter

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143