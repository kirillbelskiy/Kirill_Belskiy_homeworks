def validate_int_parameters(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return func(a, b)
    return wrapper

@validate_int_parameters
def sum(a, b):
    return a + b

try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    print(sum(a, b))
except ValueError:
    print("Ошибка: оба аргумента должны быть числами")