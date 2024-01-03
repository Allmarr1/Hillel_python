def eye_matrix(size):
    matrix = []
    for i in range(size):
        lst = []
        for j in range(size):
            if i == j:
                lst.append(1)
            else:
                lst.append(0)
        matrix.append(lst)
        # print(lst)
    return matrix

assert eye_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
