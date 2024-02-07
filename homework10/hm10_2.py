import random
import csv
import json

numbers = [random.randint(1, 100) for _ in range(100)]

with open('numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(0, len(numbers), 10):
        writer.writerow(numbers[i:i+10])

with open('numbers.json', 'w') as file:
    for i in range(0, len(numbers), 10):
        json.dump(numbers[i:i+10], file)
        file.write('\n')

csv_data = []
with open('numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        csv_data.append(list(map(int, row)))

json_data = []
with open('numbers.json', 'r') as file:
    for line in file:
        json_data.append(json.loads(line))

csv_ave = [sum(row) / len(row) for row in csv_data]
json_ave = [sum(row) / len(row) for row in json_data]

print('lineNum\tjson_ave\tcsv_ave')
for i in range(10):
    print(f"{i}\t{json_ave[i]:.2f}\t\t{csv_ave[i]:.2f}")