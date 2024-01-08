def second_smallest(a):
    min_val = a[0]
    for i in range(len(a)-1):
        sec_val = a[i+1]
        if min_val != sec_val:
            break
    if not min_val < sec_val:
        min_val, sec_val = sec_val, min_val
    for i in range(len(a)-2):
        x = a[i+2]
        if x < min_val:
            min_val, sec_val = x, min_val
        elif x < sec_val and not x == min_val:
            sec_val = x

    return sec_val

assert second_smallest([1, 1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1