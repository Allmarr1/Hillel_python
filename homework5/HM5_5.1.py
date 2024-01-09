def join_ints(my_list):
    num = ''
    for i in my_list:
        if isinstance(i, int):
            num += str(i)
    # print(int(num))

    return int(num)

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143