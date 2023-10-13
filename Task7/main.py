import Vector as vector
import Student as student
import Iterator as iterator

vect = vector.Vector(1, 2, 3, 4)
print('-' * 30)
print('            TASK 1           ')
print('-' * 30)
print(vect)

print('-' * 30)

print(vect.len())

print('-' * 30)
print(vect.ispPerpendicular(vector.Vector(1, 2, 3, 4)))

print('-' * 30)
print(vect * vector.Vector(1, 2, 3, 5))

print('-' * 30)
print(vect + vector.Vector(1, 2, 3, 4))

print('-' * 30)
print(vect == vector.Vector(1, 2, 3, 4))

print('-' * 30)
print(vect == vector.Vector(1, 2, 3, 5))

print('-' * 30)
print('            TASK 2           ')

student1 = student.Student('Nazar', {'Math': [5, 4, 5, 5], 'English': [4, 5, 5, 5], 'History': [5, 5, 5, 5]})
student2 = student.Student('Bob', {})

print('-' * 30)
print(student1)
print(student2)

print('-' * 30)
print(student1.subject())
print(student2.subject())

print('-' * 30)
print(student1.markBySubject('Math'))
print(student2.markBySubject('Math'))

print('-' * 30)
print(student1.averageMarkBySubject('Math'))
print(student2.averageMarkBySubject('Math'))

print('-' * 30)
print(student1.averageMark())
print(student2.averageMark())

print('-' * 30)

print(student1.isCredited())
print(student2.isCredited())

print('-' * 30)
student1.addSubject('Math', [5, 5, 5, 5])
print(student1)
student2.addSubject('Math', [])
print(student2)

print('-' * 30)
student1.addMark('Math', 3)
print(student1)
student2.addMark('English', 5)
print(student2)

print('-' * 30)
print(student1.calculate_average())
print(student2.calculate_average())

print('-' * 30)
print('            TASK 3           ')

iterator1 = iterator.Iterator(1, 4, 1)
list1 = []

print('-' * 30)
for num in iterator1:
    list1.append(num)

print(list1)

print('-' * 30)
