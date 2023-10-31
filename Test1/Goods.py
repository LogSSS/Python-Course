class Goods:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} {self.price} {self.quantity}'

    def uahToUsd(self):
        print(self.name, round(self.price / 28.3, 2))

    def pricePerQuantity(self):
        price = self.quantity * self.price
        price = round(price, 2)
        print(self.name, 'is', price)

    def decreaseQuantity(self, numb):
        if self.quantity - numb >= 0:
            self.quantity -= numb
        else:
            print('Not enough quantity in', self.name, 'to decrease')

    def addPrice(self, numb):
        self.price += numb
