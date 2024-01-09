def my_split(my_str, separ):
    result = []
    temp = ''
    for i in my_str:
        if i == separ:
            result.append(temp)
            temp = ''
        else:
            temp += i

    # print(temp)
    # print (result)

    result.append(temp)
    return result

assert my_split("Karamba", "a") == ['K', 'r', 'mb', '']