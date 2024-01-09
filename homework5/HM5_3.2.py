def list_to_string(array):
    for i in range(len(array)):
        array[i] = str(array[i])
    return ''.join(array)

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"