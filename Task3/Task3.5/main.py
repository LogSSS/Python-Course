group = [{"surname": "Bruh", "name": "Knish", "marks": [5, 5, 4]},
         {"surname": "Gryniam", "name": "VlaDICKslave", "marks": [5, 5, 5]},
         {"surname": "Kolos", "name": "Vlad", "marks": [2, 1, 3]},
         {"surname": "Biba", "name": "Bob", "marks": [3, 4, 1]},
         {"surname": "Boba", "name": "Bib", "marks": [4, 5, 2]}]

print("-" * 100)
print("First student:")
print(group[0])

print("-" * 100)
print("All students:")
for i in group:
    print(i["surname"].ljust(15), i["name"].ljust(15), i["marks"])

print("-" * 100)
avgDict = {}
for i in group:
    avgDict[i["surname"]] = sum(i["marks"])/len(i["marks"])
print("Average marks:", avgDict)

print("-" * 100)
listSur = list()
for i in group:
    listSur.append(i["surname"])
print("List of surnames:", listSur)

print("-" * 100)
avgMark = 0
for i in group:
    avgMark += sum(i["marks"])/len(i["marks"])
avgMark = avgMark/len(group)
print("The average value of all average marks:", avgMark)
