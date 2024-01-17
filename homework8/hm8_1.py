# list1= [1,2,3]

# list2 = [2,4,7,3]

def good_pair(input_data):
    counter = 0
    for i in range(len(input_data[0])):
        for j in range(len(input_data[1])):
            if input_data[0][i] == input_data[1][j] and i < j:
                counter += 1
    return counter


assert good_pair(([1,2,3], [1,2,7,3])) == 1#3
assert good_pair(([1,2,3,4], [1,2,7,3,4])) == 2
