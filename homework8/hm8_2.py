def less_then_n_count(input_data):
    result = []
    for i in range(len(input_data)):
        count = 0
        for j in range(len(input_data)):
            if input_data[j] < input_data[i]:
                count += 1
        result.append(count)
    return result




assert less_then_n_count([6,5,4,8]) ==[2,1,0,3]
assert less_then_n_count([7,7,7,7]) == [0,0,0,0]

