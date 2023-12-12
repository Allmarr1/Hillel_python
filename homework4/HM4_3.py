a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b:
    for i in range(a - 1, b, -1):
        print(i)
else:
    print("Введені числа рівні.")