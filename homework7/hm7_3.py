def expanded_list(nested_list):
    list1 = []
    for i in nested_list:
        if isinstance(i, list):
            list1.extend(expanded_list(i))
        else:
            list1.append(i)
    # print(list1)
    return list1

assert expanded_list([1, 2, 3, 'hello', [7, 8, [5, 7], 9], 'world', [77, 88, 99]]) == [1, 2, 3, 'hello', 7, 8, 5,7, 9, 'world', 77, 88, 99]