# def check_curr(kasa, amount):

#     for key in kasa:
#         max_amount = amount // key
#         if max_amount > kasa[key]:
#             amount = amount - key*kasa[key]#kasa[key] - кількість купюр номіналу key що є в касі
#         else:
#             amount = amount - max_amount*key
#     if amount != 0:
#         return False
#     return True


def check_curr(kasa, amount):
    if amount == 0:
        return True
    for key in kasa:
        if amount >= key and kasa[key] > 0:
            kasa[key] -= 1
            if check_curr(kasa, amount - key):
                return True
            kasa[key] += 1
        print(kasa[key])    
    return False



assert check_curr({500:1, 100:2, 1:10}, 200) == True
assert check_curr({100:2, 1:10}, 211) == False
assert check_curr({100:2, 2:10}, 201) == False
assert check_curr({100:2, 1:10}, 57) == False