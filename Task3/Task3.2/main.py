X = [1, 4, 3, 5]
Y = [-2, 1, 3]
Q = set(X).intersection(Y)
print("X ∩ Y is", Q)

X = [1, 4, -3, 5]
Q = set(X).symmetric_difference(Y)
print("X Δ Y is", Q)
