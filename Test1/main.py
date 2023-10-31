import Finder as find
import Student as st
import decorator as dec
import Goods as gd

#########################################################
print('-' * 30)
print('           Task1           ')

text = "The quick brown fox jumps over the lazy dog. Apple is amazing"

print('Count of words starting with a or A is: ', find.Task1(text))

#########################################################
print('-' * 30)
print('           Task2           ')

students = [
    {'name': 'Bob', 'marks': [5, 4, 5]},
    {'name': 'Alice', 'marks': [4, 5, 5]},
    {'name': 'John', 'marks': [5, 5, 5]},
    {'name': 'Ann', 'marks': [4, 4, 4]},
    {'name': 'Jack', 'marks': [5, 4, 4]},
    {'name': 'Kate', 'marks': [4, 5, 4]},
    {'name': 'Mike', 'marks': [4, 4, 5]},
    {'name': 'Jane', 'marks': [5, 5, 4]},
    {'name': 'Tom', 'marks': [4, 4, 4]},
    {'name': 'Lol', 'marks': [5, 5, 5]}
]

st.Task2(students)

#########################################################
print('-' * 30)
print('           Task3           ')

numb = 3
dec.Task3(numb)

#########################################################
print('-' * 30)
print('           Task4           ')

apple = gd.Goods('Apple', 100, 10)
banana = gd.Goods('Banana', 200, 20)
orange = gd.Goods('Orange', 300, 30)

print("\nGoods:")
print(apple)
print(banana)
print(orange)

print("\nGoods in usd")
apple.uahToUsd()
banana.uahToUsd()
orange.uahToUsd()

print("\nPrice per quantity")
apple.pricePerQuantity()
banana.pricePerQuantity()
orange.pricePerQuantity()

print("\nDecrease quantity")
apple.decreaseQuantity(5)
banana.decreaseQuantity(25)
orange.decreaseQuantity(5)

print("\nAdd price")
apple.addPrice(5)
banana.addPrice(25)
orange.addPrice(5)

print("\nGoods:")
print(apple)
print(banana)
print(orange)
