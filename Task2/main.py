from random import randrange as rd

# 1
print('-' * 30)
a = []

for i in range(int(input())):
    a.append(int(input()))

print('\n')
print(a)
print('\n')
print(len(a))
print('\n')
del a[0]
print(a)
print('\n')
print(len(a))

# 2
print('-' * 30)
b = [4, 6, 23, 35]  # ПОПЕРЕДНІЙ МАСИВ
n = int(input())

for i in range(n):
    a.append(rd(1, 10))

print(a)
b += a
print(f"\n{b}")

# 3
print('-' * 30)
word = input()
arr = list(word)
print(arr)

# Main Task
MENU = """<======================>
My menu
1: create list
2: add element
3: preview
4: exit
5: create ranged list
6: change at
7: insert at
8: delete at"""

isCreated = False

while 1:
    print(MENU)
    x = int(input())

    if x == 1:
        arr = []
        isCreated = True
        print(" > DONE")
        continue

    if x == 2:
        if not isCreated:
            print(" > Create list PLS :D")
            continue
        print(" > Element:")
        while 1:
            try:
                val = int(input())
                break
            except ValueError:
                print(" > NOT number\n > Try again:")
        arr.append(val)
        continue

    if x == 3:
        if not isCreated:
            print(" > Create list PLS :D")
            continue
        print(arr)
        continue

    if x == 4:
        print(" > BYE")
        break

    if x == 5:
        print(" > Length of list:")
        while 1:
            try:
                size = int(input())
                if size <= 0:
                    print(" > Number must be positive")
                    continue
                break
            except ValueError:
                print(" > NOT number. Try again:")
        arr = list(range(size))
        isCreated = True
        print(" > Created")
        continue

    if x == 6:
        if not isCreated:
            print(" > Create list PLS :D")
            continue
        if len(arr) == 0:
            print(" > List is empty")
            continue

        print(arr)
        print(len(arr))
        print(" > Input pos to change")
        while 1:
            try:
                pos = int(input())
                if pos < 0 or pos >= len(arr):
                    print(" > Pos out of bound")
                    continue
                break
            except ValueError:
                print(" > NOT number. Try again:")

        print(" > Value to change")

        while 1:
            try:
                val = int(input())
                break
            except ValueError:
                print(" > NOT number\n > Try again:")

        arr[pos] = val
        print(" > Changed")
        continue

    if x == 7:
        if not isCreated:
            print(" > Create list PLS :D")
            continue

        print(arr)
        print(len(arr))
        print(" > Input pos to add")

        while 1:
            try:
                pos = int(input())
                if pos < 0:
                    print(" > Pos is negative")
                    continue
                break
            except ValueError:
                print(" > NOT number. Try again:")

        print(" > Value to add")

        while 1:
            try:
                val = int(input())
                break
            except ValueError:
                print(" > NOT number\n > Try again:")

        arr.insert(pos, val)
        print(" > Added")

        continue

    if x == 8:
        if not isCreated:
            print(" > Create list PLS :D")
            continue
        if len(arr) == 0:
            print(" > List is empty")
            continue

        print(arr)
        print(len(arr))
        print(" > Input pos to del")
        while 1:
            try:
                pos = int(input())
                if pos < 0 or pos >= len(arr):
                    print(" > Pos out of bound")
                    continue
                break
            except ValueError:
                print(" > NOT number. Try again:")

        arr.pop(pos)
        print(" > Deleted")
        if len(arr) == 0:
            isCreated = False
            print(" > List is empty BTW")

    print(f" > No option for {x}")
    continue
