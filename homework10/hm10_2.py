import csv
import json
import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

with open('random_numbers.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['col{}'.format(i) for i in range(10)])  
    for i in range(0, 100, 10):
        csv_writer.writerow(random_numbers[i:i + 10])

json_data = {'data': [random_numbers[i:i + 10] for i in range(0, 100, 10)]}
with open('random_numbers.json', 'w') as json_file:
    json.dump(json_data, json_file, indent = 2)

with open('random_numbers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    csv_data = [list(map(int, row)) for row in csv_reader]

with open('random_numbers.json') as json_file:
    json_data = json.load(json_file)
    json_data = json_data['data']

csv_averages = [sum(row) / len(row) for row in csv_data]
json_averages = [sum(row) / len(row) for row in json_data]

print("lineNum\tjson_ave\tcsv_ave")
for i in range(10):
    print(f"{i}\t{json_averages[i]:.2f}\t\t{csv_averages[i]:.2f}")