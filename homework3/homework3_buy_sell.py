UAN_USD = 38
UAN_EUR = 41
UAN_PLN = 9
uah = int(input("Введіть суму в гривні "  ))
operation = str(input("Виберить операцію: 'B-купівля', 'S-продаж', 'Все разом-A' "))

buy1 = int(uah // UAN_USD)
buy2 = int(uah // UAN_EUR)
buy3 = int(uah // UAN_PLN)
sell1 = int(buy1 + buy1 * 0.05)
sell2 = int(buy2 + buy2 * 0.05)
sell3 = int(buy3 + buy3 * 0.05)

left_buy1 = int(uah % UAN_USD)
left_buy2 = int(uah % UAN_EUR)
left_buy3 = int(uah % UAN_PLN)

left_sell1 = int(sell1 * UAN_USD - uah)
left_sell2 = int(sell2 * UAN_EUR - uah)
left_sell3 = int(sell3 * UAN_PLN - uah)



if operation == 'B':
    print("*" * 17)

    print(f"*{'':<7}BUY{'':>5}*")

    print(f"*{buy1:<5}{'':>8}USD")
    print(f"*{buy2:<5}{'':>8}EUR")
    print(f"*{buy3:<5}{'':>8}PLN")

    print("*" * 17)
    print("Ваша решта UAH")
    print(f"*{left_buy1:<5}решта з USD")
    print(f"*{left_buy2:<5}решта з EUR")
    print(f"*{left_buy3:<5}решта з PLN")

elif operation == 'S':
    print("*" * 17)

    print(f"*{'':<6}SELL{'':>5}*")

    print(f"*{sell1:<5}{'':>8}USD")
    print(f"*{sell2:<5}{'':>8}EUR")
    print(f"*{sell3:<5}{'':>8}PLN")

    print("*" * 17)
    print("Ваша решта UAH")

    if left_sell1 < 0:
        print(f"З Вас ще {left_sell1} uah")
    else:
        print(f"*{left_sell1:<5}решта з USD")


    if left_sell2 < 0:
        print(f"З Вас ще {left_sell2} uah")
    else:
        print(f"*{left_sell2:<5}решта з EUR")

    print(f"*{left_sell3:<5}решта з PLN")

    print("*" * 17)
elif operation == 'A':
    print("*" * 15)

    print(f"*BUY{' ' * 6}SELL*")

    print(f"*{buy1:<5}USD{sell1:>5}*")
    print(f"*{buy2:<5}EUR{sell2:>5}*")
    print(f"*{buy3:<5}PLN{sell3:>5}*")

    print("*" * 15)
    print("Ваша решта UAH")
    print(f"*{left_buy1:<5}USD{left_sell1:>5}*")
    print(f"*{left_buy2:<5}EUR{left_sell2:>5}*")
    print(f"*{left_buy3:<5}PLN{left_sell3:>5}*")

    print("*" * 15)

else:
    print("Введіть вірне значення")


