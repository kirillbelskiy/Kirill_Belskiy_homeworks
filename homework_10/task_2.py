number = int(input("Введите число, для которого хотите вывести таблицу умножения: "))
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

multiplication_table(number)
