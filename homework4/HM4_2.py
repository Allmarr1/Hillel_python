sum = 0

while True:
    u_input = input("Введіть число або введіть end та отримайте суму всіх чисел: ")

    if u_input == 'end':
        break
    if u_input.isdigit():
        numbers = int(u_input)
        sum += numbers
    else:
        print("Невірний формат")

print("Сума введених чисел:", sum)

