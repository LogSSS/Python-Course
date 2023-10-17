import Decorator as dec

# First

print("-" * 30)
print("            TASK 1           ")
print("-" * 30)


@dec.Decorator.makeBold
@dec.Decorator.makeItalic
def hello(str: str) -> None:
    print(str)


hello("Hello world!")


@dec.Decorator.makeItalic
@dec.Decorator.makeBold
def hello(str: str) -> None:
    print(str)


hello("Hello world!")

# Second

print("-" * 30)
print("            TASK 2           ")
print("-" * 30)


@dec.Decorator.palindrome
def palindrome(str1: str) -> bool:
    return str1 == str1[::-1]


print(palindrome("Я несу гусеня"))
print(palindrome("БОБІк"))

# Third

print("-" * 30)
print("            TASK 3           ")
print("-" * 30)


@dec.Decorator.check
def check(dict: dict) -> dict:
    return {v: k for k, v in dict.items()}


print(check({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}))

print(check({"a": 1, "b": 2, "c": 3, "d": 4, "e": 4}))

# Fourth

print("-" * 30)
print("            TASK 4           ")
print("-" * 30)


@dec.Decorator.validate
def validate(arr: list | tuple) -> bool:
    if len(arr) != len(set(arr)):
        return False
    return True


print("List:")
print(validate([1, 2, 3, 4, 5]))  # list
print(validate([1, 2, 3, 4, 5, 5]))

print("Tuple:")
print(validate((1, 2, 3, 4, 5)))  # tuple
print(validate((1, 2, 3, 4, 5, 5)))

print("Sequence:")
print(validate({1, 2, 3, 4, 5}))  # sequence
print(validate({1, 2, 3, 4, 5, 5}))

print("Dict:")
print(validate({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}))  # dict
print(validate({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 5}))

print("String:")
print(validate("12345"))  # str
print(validate("123455"))

print("Int:")
print(validate(12345))  # int
print(validate(123455))

print("Float:")
print(validate(123.45))  # float
print(validate(123.455))

print("-" * 30)
