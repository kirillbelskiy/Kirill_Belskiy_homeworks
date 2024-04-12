def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    else:
        return x / y

def exit_program(x, y):
    print("Завершение программы")
    exit()

while True:
    operation = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if operation == '+':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = add(num1, num2)
        print("Результат: ", result)
    elif operation == '-':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = subtract(num1, num2)
        print("Результат: ", result)
    elif operation == '*':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = multiply(num1, num2)
        print("Результат: ", result)
    elif operation == '/':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if num2 == 0:
            print("Ошибка: деление на ноль")
        else:
            result = divide(num1, num2)
            print("Результат: ", result)
    elif operation == '0':
        exit_program(None, None)
    else:
        print("Неизвестная операция")
