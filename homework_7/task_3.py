A = int(input("Введите минимальное рекомендуемое количество часов сна: "))
B = int(input("Введите максимальное рекомендуемое количество часов сна: "))
H = int(input("Введите сколько часов спит Аня: "))

while A > B:
    print("Ошибка: минимальное количество часов сна не может быть больше максимального. Повторите попытку.")
    A = int(input("Введите минимальное рекомендуемое количество часов сна: "))
    B = int(input("Введите максимальное рекомендуемое количество часов сна: "))

if H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
else:
    print("Это нормально")
