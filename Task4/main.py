import random as r
import re

# 1
print('-' * 30)
a = [0] * 5
print("Нулі:", a)

# 2
print('-' * 30)
comprehension = [r.randint(0, 100) for i in range(10)]
print("Випадкові 10 чисел:", comprehension)

# 3
print('-' * 30)
a = [45, 67, 24, 45]
comprehension = {i: i % 10 for i in a}
print("Список:", comprehension)

# 4
print('-' * 30)
students = {'Shkvarok': 45, 'Gryniam': 67, 'Bilanuk': 24, 'Knish': 45, 'Kolintso': 1}
comprehension = [i for i in students if students[i] >= 50]
print("Більше 50:", comprehension)

# 5
print('-' * 30)
comprehension = [int(i) for i in 'grt743gfcg0r3' if i.isdigit()]
print("Числа:", comprehension)

# 6
print('-' * 30)
print("Сума цифр =", sum([int(i) for i in input('Введіть число: ')]))

# 7
print('-' * 30)
a = [i for i in input('Введіть елементи через пробіл: ').split()]
print("Чи всі елементи різні:", len(a) == len(set(a)))

# 8
print('-' * 30)
print(re.sub(r'[^\w\s]', ' ', input('Введіть рядок: ')))

# 9
print('-' * 30)
text1 = input('Введіть перший рядок: ')
text2 = input('Введіть другий рядок: ')
print(all(char in text1 for char in text2))

# 10
print('-' * 30)
line = {'a': 1, 'b': 2, 'c': 3}
print("Словник:", line)
print("Змінений словник:", {value: key for key, value in line.items()})

# 11
print('-' * 30)
students = ('Shkvarok', 'Gryniam', 'Bilanuk', 'Knish', 'Kolintso')
comprehension = {i: r.randint(1, 100) for i in students}
print("Словник:", comprehension)

# 12
print('-' * 30)
text = re.sub(r'[^\w\s]', ' ', input('Введіть рядок: ')).lower()
print("Словник:", {i: text.count(i) for i in text.split()})
