input_a= input("Введіть ціле число a в діапазоні від 1 до 100: ")
input_b= input("Введіть ціле число b в діапазоні від 1 до 100: ")

if input_a.isdigit() and input_b.isdigit():
    a = int(input_a)
    b = int(input_b)

    if a in range(1, 201) and b in range(1, 201):
            for j in range(2, 7):
                temp = ''
                count = 0
                for i in range(a, b):
                    if (i%j) == 0:
                        temp = temp + str(i) + ', '
                        count += 1
                        if count == 10:
                            temp = temp + (f"\n {'':>16}")
                            count = 0
                    print(f"Dividible by {j}: ", temp)
    else:
        print("Введіть ціле число в заданому діапазоні")
else:
    print("Введіть ціле число")