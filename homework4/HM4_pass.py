user_pass = input("Введіть пароль: ")

if len(user_pass) < 12:
    print("Ваш пароль занадто короткий")
else:
    if not any (i.islower() for i in user_pass):
        print("Ваш пароль небезпечний, потрібна буква у нижньому регістрі")
    elif not any (i.isupper() for i in user_pass):
        print("Ваш пароль небезпечний, потрібна буква у верхньому регістрі")
    elif not any (i.isdigit() for i in user_pass):
        print("Ваш пароль небезпечний, потрібна цифра")
    elif not any (i in '?/!@' for i in user_pass):
        print("Ваш пароль небезпечний, використовуйте один з цих символів (?/!@)")
    else:
        print("Ваш пароль надійний")