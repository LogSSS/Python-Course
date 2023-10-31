import numpy as np

# 1 data
print("-" * 30)
a = np.array([1, 2, 3])
b = np.array([2, 4, 2])

print("A: ", a)
print("B: ", b)

# 2
print("-" * 30)
ab = a + b
print("A + B: ", ab)

# 3.1
print("-" * 30)
ab = a - b
print("A - B: ", ab)

# 3.2
ab = b - a
print("B - A: ", ab)

# 4
print("-" * 30)
a = a * 2
b = b * 3
print("A * 2: ", a)
print("B * 3: ", b)

# 5
print("-" * 30)
mul = np.dot(a, b)
print("A * B: ", mul)

# 6
print("-" * 30)
lenA = np.linalg.norm(a)
lenB = np.linalg.norm(b)
print("Norm of A: ", lenA)
print("Norm of B: ", lenB)

# 7
print("-" * 30)
lenAB = np.linalg.norm(a - b)
print("Length between A and B: ", lenAB)

# 8
print("-" * 30)
angle = np.degrees(np.arccos(np.dot(a, b) / (lenA * lenB)))
print("Angle between A and B: ", angle)
