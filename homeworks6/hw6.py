PROFIT_PRC = 5  # 5%


def convert_and_sell(currency_key, val_uah):
    sell = currency_key + (currency_key * PROFIT_PRC / 100)
    result = val_uah // currency_key
    remain = val_uah % currency_key
    return result, remain, sell


### Табло курсу валют
AUH_EUR_BUY = 42.00
AUH_USD_BUY = 40.00
AUH_PLN_BUY = 30.00
AUH_EUR_CELL = AUH_EUR_BUY + (AUH_EUR_BUY * PROFIT_PRC / 100)
AUH_USD_CELL = AUH_USD_BUY + (AUH_USD_BUY * PROFIT_PRC / 100)
AUH_PLN_CELL = AUH_PLN_BUY + (AUH_PLN_BUY * PROFIT_PRC / 100)

print(f"{'':*^15}")
print(f"{'*BUY':<5}{'':5}{'SELL*':>5}")
print(f"*{AUH_EUR_BUY:<5}{'EUR':^3}{AUH_EUR_CELL:>5}*")  # loop
print(f"*{AUH_USD_BUY:<5}{'USD':^3}{AUH_USD_CELL:>5}*")  # loop
print(f"*{AUH_PLN_BUY:<5}{'PLN':^3}{AUH_PLN_CELL:>5}*")  # loop
print(f"{'':*^15}")
###

current = {
    "UAH": {
        "buy": {
            "USD": AUH_USD_BUY,
            "EUR": AUH_EUR_BUY,
            "PLN": AUH_PLN_BUY,
        },
    }
}

# while True:
#     try:
#         val_uah = float(input("Введіть кількість гривень, яку ви хочете продати: "))
#         if val_uah < current["UAH"]["buy"][currency_key]:
#             print("У Вас недостатньо коштів")
#             continue
#         break
#     except ValueError:
#         print("Лише число")
#         continue

print("Оберіть валюту, яку бажаєте отримати:")
print("1. Долар США (USD)")
print("2. Євро (EUR)")
print("3. Злотий (PLN)")

currency = input("Введіть номер валюти: ")

if currency == "1":
    currency_key = "USD"
elif currency == "2":
    currency_key = "EUR"
elif currency == "3":
    currency_key = "PLN"
else:
    print("Нажаль, такої валюти немає. Рахуємо Вам в USD.")
    currency_key = "USD"

max = 3
attempt = 0

while True:
    try:
        val_uah = float(input("Введіть кількість гривень, яку ви хочете продати: "))
        if val_uah < current["UAH"]["buy"][currency_key]:
            print("Сума недостатня, додайте для купівлі хоча б однієї одиниці валюти")
            attempt += 1
            if attempt == max:
                print('Максимальна кількість спроб! До зустрічі наступного разу')
                break
            continue
        break
    except ValueError:
        print("Лише число")
        attempt += 1
        if attempt == max:
            print('Максимальна кількість спроб! До зустрічі наступного разу')
            exit(0)


our_banknotes = {100: 2, 50: 10, 20: 0, 10: 0, 5: 100, 2: 10, 1: 10}


def check_banknotes(dictanary, amount):
    counter = 0
    for key, value in dictanary.items():
        if value <= 0:
            pass
        else:
            counter += key * value
    return counter >= amount


result, remain, sell = convert_and_sell(current["UAH"]["buy"][currency_key], val_uah)


if check_banknotes(our_banknotes, result):
    print(f"Ваша валютa {result} {currency_key}")
    print(f"Ваша решта {remain:>7} UAH")
else:
    print("Нажаль ми не можемо обміняти таку суму, недостатньо коштів")
