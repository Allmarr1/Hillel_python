u_input = input("Введіть число від 1 до 100: ")

if u_input.isdigit():
    num = int(u_input)

if 1 <= num <=100:
    print("Таблиця множення на введене число:")

    for i in range(1,11):
        result = num * i
        print(f"{num} * {i} = {result}")
    else:
        print("Введіть число від 1 до 100.")
else:
    print("Введіть ціле число.")