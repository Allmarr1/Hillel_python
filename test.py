def check_curr(kasa: dict, amount: int, keys = None):
    if keys is None:
        keys = list(kasa.keys())

    if not keys:
        return amount == 0

    key = keys[0]

    max_amount = amount // key
    if max_amount > kasa[key]:
        amount = amount - key * kasa[key]
    else:
        amount = amount - max_amount * key

    if amount == 0:
        return True
    elif amount < 0:
        return False
    else:
        del keys[0]
        return check_curr(kasa, amount, keys )





assert check_curr({500:1, 100:2, 1:10}, 200) == True
assert check_curr({100:2, 1:10}, 211) == False
assert check_curr({100:2, 2:10}, 201) == False
assert check_curr({100:2, 1:10}, 57) == False