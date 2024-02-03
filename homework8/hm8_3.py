def cesar_code(input_data):
    alphabet_length = 26
    gap = input_data[0]
    text = input_data[1]
    result = ''

    for i in text.lower():
        if i.isalpha():
            if i == 'a':
                result += chr(ord(i) + alphabet_length - gap)
            else:
                result += chr(ord(i) - gap)
        else:
            result += i

    return result

assert cesar_code((1, "az")) == "zy"
assert cesar_code((3, "az")) == "xw"

