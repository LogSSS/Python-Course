import functions as f

print('-' * 30)

# --------------------------------------------
# 1
n = 1234567890
result = f.countDifferentDigits(n)
print(f"The number of different digits in the number {n}: {result}")
print('-' * 30)

n = 12345678
print(f"The number {n} is missing the following digits: {f.getMissingDigits(n)}")
print('-' * 30)

# --------------------------------------------
# 2
text1 = "((())())"
text2 = "(())f.)("

print(f"Result for text '{text1}': {f.isParentheses(text1)}")
print(f"Result for text '{text2}': {f.isParentheses(text2)}")
print('-' * 30)

# --------------------------------------------
# 3
sentence = "Hello world. How are you today?"

print("All the vowels included in each word:", f.findVowelsInEachWord(sentence))
print("All vowels that are not included in any word", f.findVowelsNotInAnyWord(sentence))
print("All letters included in the line at least twice:", f.findRepeatedLetters(sentence))
print("All letters included in the string once:", f.findUniqueLetters(sentence))
print('-' * 30)

# --------------------------------------------
# 4
i = 1
for result in f.factorialGenerator(1, 10):
    print(f"The factorial of {i} is: {result}")
    i += 1

print('-' * 30)

# --------------------------------------------
# 5

print(f.task("Bruh asd asd bob S. BOB."))
print('-' * 30)

print(f.tasK([1, 2, 3, 4, 5, 6, 7, 9, 9]))
print('-' * 30)

print(f.task2("Bruh. BOB."))
print('-' * 30)

print(f.task3(2, 3))
print('-' * 30)

print([f.task4(data) for data in [(1, 2), (3, 4), (5, 6), (7, 8)]])
print('-' * 30)

print(f.gen_binary())
print('-' * 30)

# --------------------------------------------
