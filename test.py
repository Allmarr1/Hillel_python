import random
import csv
import json


numbers = [random.randint(1, 100) for _ in range(100)]


with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0, len(numbers), 10):
        writer.writerow(numbers[i:i+10])


with open('numbers.json', 'w') as file:
    json.dump([numbers[i:i+10] for i in range(0, len(numbers), 10)], file)


csv_data = []
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        csv_data.append(list(map(int, row)))

with open('numbers.json', 'r') as file:
    json_data = json.load(file)


csv_ave = [sum(row) / len(row) for row in csv_data]
json_ave = [sum(row) / len(row) for row in json_data]


print('lineNum', 'json_ave', 'csv_ave')
for i in range(10):
    print(i, json_ave[i], csv_ave[i])
