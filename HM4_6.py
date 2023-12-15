n = 7


for i in range(n - 4, n + 4):
    for j in range(2, 10):
        res = str(i*j)
        print(j, '*', str(i).rjust(2), '=', res.rjust(3), end='   ')
    print()

# a=5
# b=100
