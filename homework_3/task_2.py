a = int(input("Введите длину 1-ой стороны треугольника:"))
b = int(input("Введите длину 2-ой стороны треугольника:"))
c = int(input("Введите длину 3-ей стороны треугольника:"))
if a + b > c and a + c > b and b + c > a:
    print(f"Треугольник со сторонами {a},{b},{c} - существует")
else:
    print(f"Треугольник со сторонами {a},{b},{c} - не существует")