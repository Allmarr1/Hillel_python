u_input = input("Введіть число від 6 до 16: ")
if u_input.isdigit():
    n = int(u_input)

    if 6<= n <= 16:
        for i in range(n - 4, n + 4):
            for j in range(2, 10):
                res = str(i*j)
                print(j, '*', str(i).rjust(2), '=', res.rjust(3), end='   ')
            print()
    else:
        print("Ви ввели число поза межами заданого діапазону")

else:
    print("Введіть ціле число")
