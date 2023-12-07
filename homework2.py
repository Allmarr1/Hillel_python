UAN_USD = 37.55
UAN_EUR = 40.50
UAN_PLN = 9.45
uah = int(input("print amount of uah"  ))

buy1 = uah // UAN_USD
buy2 = uah // UAN_EUR
buy3 = uah // UAN_PLN
sell1 = buy1 + buy1 * 0.05
sell2 = buy2 + buy2 * 0.05
sell3 = buy3 + buy3 * 0.05
print(f"{:*>15}")
print(f"*{buy1:*>5}" "USD" f"{sell1:*<5}*")
print(f"*{buy2:*>5}" "USD" f"{sell2:*<5}*")
print(f"*{buy3:*>5}" "USD" f"{sell3:*<5}*")

print(f" {1:*>4}")