import numpy as np


def second():
    # 1
    print("-" * 30)
    a = np.array([[1, 2, 3, -2], [1, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]])
    b = np.array([6, 8, 4, -8])
    print("Equations: ")
    printEq(a, b)

    # 2
    print("-" * 30)
    solve = np.linalg.solve(a, b)
    print("x using solve: ", solve)

    # 3
    print("-" * 30)
    a_inv = np.linalg.inv(a)
    inv = np.dot(a_inv, b)
    print("x using inv: ", inv)

    # 4
    print("-" * 30)
    det_a = np.linalg.det(a)
    kramer = np.zeros(a.shape[1])
    for i in range(a.shape[1]):
        temp = a.copy()
        temp[:, i] = b
        kramer[i] = np.linalg.det(temp) / det_a

    print("x using kramer: ", kramer)

    # 5
    print("-" * 30)
    print("Equal 1st(solve func) and 2nd(inv): ", np.allclose(solve, inv))
    print("Equal 1st(solve func) and 3rd(kramer): ", np.allclose(solve, kramer))
    print("Equal 2nd(inv) and 3rd(kramer): ", np.allclose(inv, kramer))

    # 6 data
    print("-" * 30)
    a = np.matrix([[4, 5, -2], [3, -1, 0], [4, 2, 7]])
    b = np.matrix([[2, 1, -1], [0, 1, 3], [5, 7, 3]])
    print("Matrix A: \n" + str(a))
    print("Matrix B: \n" + str(b))

    # 7
    print("-" * 30)
    result = 3 * a - np.dot((a - 2 * b), b)
    # can be result = 3 * a - (a - 2 * b) * b
    print("Result of 3 * a - (a - 2 * b) * b: \n" + str(result))

    print("-" * 30)


def printEq(a, b):
    for i in range(len(a)):
        equation = ''
        for j in range(len(a[i])):
            if a[i][j] != 0:
                if a[i][j] == 1:
                    equation += f'X{j + 1} '
                elif a[i][j] == -1:
                    equation += f'- X{j + 1} '
                else:
                    equation += f'{a[i][j]} * X{j + 1} '

                if j != len(a[i]) - 1 and a[i][j + 1] != 0:
                    equation += '+ ' if a[i][j + 1] >= 0 else ''

        equation += f'= {b[i]}'
        print(equation)
