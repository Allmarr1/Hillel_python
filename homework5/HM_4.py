def list_intercection(list1, list2):

    x = set(list1)
    y = set(list2)
    list3 = list(x.intersection(y))

    print(list3)

    if list3:
        return list3
    else:
        return None

# print(list_intercection(["foo", 1, "bar"], [])) 




assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1, ]
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]