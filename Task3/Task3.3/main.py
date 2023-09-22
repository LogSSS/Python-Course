marks = {'Feduk': [5, 3, 2, 5],
         'Borosnuk': [4],
         'Denis': [2, 3, 1],
         'Gryniam': [5, 5, 5, 5, 5],
         'Nazarko': [4, 5, 3, 4],
         }

middleMarks = dict()
for i in marks:
    sum = 0
    for j in marks[i]:
        sum += j
    middleMarks[i] = sum/len(marks[i])

count = 0
for i in marks:
    for j in marks[i]:
        if(j < 3):
            count += 1
print("Кількість заборгованостей: " + str(count))

print()

print("Середній бал кожного учня:")
for i in middleMarks:
    print(i + ": " + str(middleMarks[i]))
