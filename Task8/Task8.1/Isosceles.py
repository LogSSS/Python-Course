import Triangle as tri
import math


class Isosceles(tri.Triangle):

    def __init__(self, a: float, basis: float) -> None:
        super().__init__(a, basis, a)

    def area(self) -> float:
        return math.sqrt(self.a * self.a - self.b * self.b / 4) * self.b / 2
