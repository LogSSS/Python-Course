import numpy as np

# 1 data
temperature = np.array([4, 1, 0, -2, 5, 7, -3, 0, 0, 5, 0, -1, 3, 6, 9, 5, 7, 11, 9, 6, 0])

# 2
print("Temperature: ", temperature)

# 3
highest = np.max(temperature)
print("Highest temperature: ", highest)

# 4
highest_id = np.argmax(temperature)
print("Highest temperature id: ", highest_id)

# 5
temperature[highest_id] = 0
print("Temperature: ", temperature)

# 6
below_zero = len(temperature[temperature < 0])
print("Days below zero: ", below_zero)

# 7.1
greater_than_10 = np.any(temperature > 10)
print("Greater than 10: ", greater_than_10)

# 7.2
greater_than_20 = np.any(temperature > 20)
print("Greater than 20: ", greater_than_20)

# 8
all_less_than_10 = np.all(temperature < 10)
print("All less than 10: ", all_less_than_10)

# 9
size = np.size(temperature)
print("Size: ", size)

# 10
random_array = np.random.randint(-5, 5, 31 - size)
print("Random array: ", random_array)

# 11
union = np.union1d(temperature, random_array)
print("Union: ", union)

# 12
np.sort(union)
print("Sorted union: ", union)
