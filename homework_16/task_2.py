import math

class RightTriangle:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)

    def resize(self, percent):
        self.a += self.a * percent / 100
        self.b += self.b * percent / 100
        self.c = math.sqrt(self.a**2 + self.b**2)

    def circumscribed_radius(self):
        return self.c / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def angles(self):
        alpha = math.degrees(math.asin(self.a / self.c))
        beta = math.degrees(math.asin(self.b / self.c))
        gamma = 90
        return alpha, beta, gamma

triangle = RightTriangle(3, 4)
print(f"Периметр треугольника: {triangle.perimeter()}")
print(f"Радиус описанной окружности: {triangle.circumscribed_radius()}")
triangle.resize(10)
print(f"Новый периметр треугольника: {triangle.perimeter()}")
alpha, beta, gamma = triangle.angles()
print(f"Значения углов треугольника: α = {alpha}, β = {beta}, γ = {gamma}")
