import Triangle as tr
import Isosceles as iso

triangle = tr.Triangle(3, 4, 5)

print("-" * 30)
print('            TASK 1           ')
print("-" * 30)
print(triangle.perimeter())
print(triangle.area())

print("-" * 30)
print('            TASK 2           ')
print("-" * 30)

isosceles = iso.Isosceles(3, 4)
print(isosceles.perimeter())
print(isosceles.area())
