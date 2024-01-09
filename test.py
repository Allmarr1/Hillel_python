def join_ints(my_list):
    result = 0

    for item in my_list:
        if isinstance(item, int):
            result = result * 10 + item
    print(result)
    return result

# Тести
assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143