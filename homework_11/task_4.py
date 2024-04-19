import math
def calculate_circle_p(radius):
    return 2 * math.pi * radius

radius = float(input("Введите радиус круга: "))
circle_p = calculate_circle_p(radius)

print(f"Периметр круга с радиусом {radius} равен {circle_p}")
