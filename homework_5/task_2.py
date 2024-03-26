while True:
    operation = input("Введите операцию (+, -, *, /, **, //, % или 0 для выхода): ")
    if operation == '0':
        print("Программа завершена")
        break

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '**':
        result = num1 ** num2
    elif operation == '//':
        if num2 != 0:
            result = num1 // num2
        else:
            print("Ошибка: деление на ноль")
            continue
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            print("Ошибка: деление на ноль")
            continue
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль")
            continue
    else:
        print("Неверная операция")
        continue

    print(f"Результат: {result}")
