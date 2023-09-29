import csv
from prettytable import PrettyTable

results = {'відмінно': 0, 'добре': 0, 'задовільно': 0}

with open('KN-2.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_score = int(row["Test"])
        if test_score >= 90:
            results['відмінно'] += 1
        elif 70 <= test_score < 90:
            results['добре'] += 1
        elif 50 <= test_score < 70:
            results['задовільно'] += 1

table = PrettyTable()
table.field_names = ['Оцінка', 'Кількість']
for category, count in results.items():
    table.add_row([category, count])

print(table)
