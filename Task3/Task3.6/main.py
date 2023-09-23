list1 = ['good', 'better', 'the best']
list2 = [4, 0, 4]

print("-" * 30)
print("-", "Lists".center(26, " "), "-")
print("-" * 30)
listTuple1 = tuple(list1)
listTuple2 = tuple(list2)
print(listTuple1)
print(listTuple2)

print("-" * 30)
listSet1 = set(list1)
listSet2 = set(list2)
print(listSet1)
print(listSet2)

print("-" * 30)
listDict = dict(zip(list1, list2))
print(listDict)

print("-" * 30)
listStr1 = " ".join(list1)
listStr2 = " ".join(map(str, list2))
print(listStr1)
print(listStr2)

print("-" * 30)
list3 = list1 + list2
print(list3)

print("-" * 30)
print("-", "Plural".center(26, " "), "-")
print("-" * 30)
plural = {'Сидоренко', 'Петрів', 'Дорош'}

listPlural = list(plural)
print(listPlural)
tuplePlural = tuple(plural)
print(tuplePlural)

print("-" * 30)
dictPlural = dict.fromkeys(plural, 100)
print(dictPlural)

print("-" * 30)
plural.update({'Вітенко', 'Дорош'})
print(plural)

print("-" * 30)
print("-", "Dictionary".center(26, " "), "-")
print("-" * 30)

dict1 = {'Denys': 45, 'Olek': 89, 'Ivan': 100}
dictList = list(dict1.keys())
print(dictList)

print("-" * 30)
dictTuple = tuple(dict1.values())
print(dictTuple)

print("-" * 30)
dictStr = " ".join(dict1.keys())
print(dictStr)

print("-" * 30)
dict1.update({'Сидоренко': 34})
print(dict1)

print("-" * 30)
print("-", "Str".center(26, " "), "-")
print("-" * 30)

str1 = "all right"
strList = list(str1)
print(strList)

print("-" * 30)
strList2 = str1.split()
print(strList2)

print("-" * 30)
strDict = dict.fromkeys(strList2, None)
print(strDict)

print("-" * 30)
print("-", "TaskA".center(26, " "), "-")
print("-" * 30)
while 1:
    try:
        listNumb = input("Enter numbers('exit' for exit :D): ").split()
        if listNumb[0] == "exit":
            break
        listNumb = list(map(int, listNumb))
        if len(listNumb) == 3:
            x, y, z = listNumb
            print(x, y, z)
        elif len(listNumb) < 3:
            print("MORE NUMBERS!!!")
        else:
            head, *middle, tail = listNumb
            print(head, middle, tail)
    except ValueError:
        print("Input values must be integer")
    print("-" * 30)
