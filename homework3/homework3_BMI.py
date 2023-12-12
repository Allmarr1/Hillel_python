weight_unit  = input("Виберіть одиниці вибору ваги (k=kg, l=lb)")
if  weight_unit not in ['k', 'l']:
    print("Невідомі одиниці виміру ваги")
    exit()

height_unit  = input("Виберіть одиниці вибору зросту (m=m, i=in)")
if  height_unit not in ['m', 'i']:
    print("Невідомі одиниці виміру зросту")
    exit()

weight = float(input("Введіть Вашу вагу "))
height = float (input("Введіть Ваш зріст "))

if weight_unit == 'l':
    weight = weight * 0.453592

if height_unit == 'i':
    height = height * 0.0254

bmi = weight / (height ** 2)

print("Ваш індекс ваги = ", bmi)

if bmi < 18.5:
    print("У Вас недостатня вага")
elif 18.5 <= bmi < 24.9:
    print("У Вас нормальна вага")
elif 25 <= bmi < 29.9:
    print("У Вас надлишкова вага")
else:
    print("У Вас ожиріння")






