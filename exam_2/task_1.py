class TriangleChecker:
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Все длины отрезков должны быть положительными числами")

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        else:
            return "Жаль, но из этого треугольник не сделать."

try:
    a = float(input("Введите длину первого отрезка: "))
    b = float(input("Введите длину второго отрезка: "))
    c = float(input("Введите длину третьего отрезка: "))
    checker = TriangleChecker(a, b, c)
    result = checker.is_triangle()
    print(result)
except ValueError as e:
    print(f"Ошибка: {e}")
