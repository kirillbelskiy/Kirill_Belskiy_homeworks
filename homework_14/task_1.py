class Calculator:
    def check_validity(self, num1, num2):
        try:
            num1, num2 = float(num1), float(num2)
        except ValueError:
            return False, None, None
        return True, num1, num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль невозможно"

calculator = Calculator()

while True:
    x = input("Введите назвнание операции(+,-,/,* или 0 для завершения работы): ")
    if x == "0":
        break
    num1 = input("Введите 1-ое число: ")
    num2 = input("Введите 2-ое число: ")
    is_valid, num1, num2 = calculator.check_validity(num1, num2)
    while not is_valid:
        print("Оба аргумента должны быть числами")
        num1 = input("Введите 1-ое число: ")
        num2 = input("Введите 2-ое число: ")
        is_valid, num1, num2 = calculator.check_validity(num1, num2)
    if x == "+":
        print(calculator.add(num1, num2))
    elif x == "-":
        print(calculator.subtract(num1, num2))
    elif x == "*":
        print(calculator.multiply(num1, num2))
    elif x == "/":
        print(calculator.divide(num1, num2))
    else:
        print("Знак калькулятора введен неверно, повторите попытку")
