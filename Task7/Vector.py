import math as m


class Vector:

    def __init__(self, x: float, y: float, x1: float, y1: float) -> None:
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1

    def __str__(self) -> str:
        return "Vector: ({}, {}) -> ({}, {})".format(self.x, self.y, self.x1, self.y1)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.x1 == other.x1 and self.y1 == other.y1

    def __add__(self, other) -> object:
        return Vector(self.x + other.x, self.y + other.y, self.x1 + other.x1, self.y1 + other.y1)

    def len(self) -> float:
        return m.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)

    def __mul__(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.x1 * other.x1 + self.y1 * other.y1

    def ispPerpendicular(self, other) -> bool:
        return self * other == 0
