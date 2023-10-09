import random as rand


# --------------------------------------------
# 1

# Обчислення кількості різних цифр у десятковому записі натурального числа n
def countDifferentDigits(numb: int) -> int:
    digit_set = set(str(numb))
    return len(digit_set)


# Друк у порядку зростання всіх цифр, які не входять до десяткового запису натурального числа n
def getMissingDigits(numb: int) -> list[str]:
    all_digits: set[str] = set("0123456789")
    n_digits = set(str(numb))
    missing_digits = sorted(all_digits - n_digits)
    return missing_digits


# --------------------------------------------
# 2

# Перевірити, чи правильно в заданому тексті розставлені круглі дужки (тобто, чи знаходиться справа від кожної
# відкриваючої дужки відповідна їй закриваюча дужка, а зліва від кожної закриваючої - відповідна їй відкриваюча).
# Відповідь - True або False
def isParentheses(text: str) -> bool:
    stack = []

    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


# --------------------------------------------
# 3

# Всі голосні літери, які входять до кожного слова
def findVowelsInEachWord(sentence: str) -> list:
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    result = []

    for word in words:
        word_vowels = [char for char in word if char in vowels]
        result.append(''.join(word_vowels))

    return result


# Всі голосні літери, які не входять до жодного слова
def findVowelsNotInAnyWord(sentence: str) -> str:
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    all_word_vowels = set()

    for word in words:
        word_vowels = set(char for char in word if char in vowels)
        all_word_vowels.update(word_vowels)

    return ''.join(char for char in vowels if char not in all_word_vowels)


# Всі літери, що входять до рядка не менше двох раз
def findRepeatedLetters(sentence: str) -> list[str]:
    char_count = {}
    for char in sentence:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return [char for char, count in char_count.items() if count >= 2]


# Всі літери, що входять до рядка по одному разу
def findUniqueLetters(sentence: str) -> str:
    char_count = {}
    for char in sentence:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return ''.join(char for char, count in char_count.items() if count == 1)


# --------------------------------------------
# 4

# Знаходження факторіалу числа n
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Генератор факторіалів
def factorialGenerator(start: int, end: int):
    for i in range(start, end + 1):
        yield factorial(i)


# --------------------------------------------
# 5
def task(b: str) -> dict[str, int]:
    return {i: b.count(i) for i in b.split()}


def tasK(a: list[int]) -> bool:
    return len(a) == len(set(a))


def task2(surnames: str) -> dict[int, str]:
    rnd_mark = tuple(rand.sample(range(1, 100), 5))
    stud = {rnd_mark[i]: surnames[i] for i in range(len(rnd_mark))}
    return stud


def task3(cols: int, rows: int) -> list[list[int]]:
    a = [[1 if not (i + j) % 2 else 0 for j in range(cols)] for i in range(rows)]
    return a


def task4(data: tuple[int, int]) -> tuple[int, int]:
    x, y = data
    return x * 2, y * 2


def gen_binary() -> str:
    while True:
        for x in range(2):
            for y in range(2):
                yield str(x) + str(y)

# --------------------------------------------
