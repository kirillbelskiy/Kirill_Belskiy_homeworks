def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Введите число, для которого хотите вывести таблицу умножения: "))
multiplication_table(n)
