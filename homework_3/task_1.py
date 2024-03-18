year = int(input("Введите год:"))


if year % 4 != 0:
    print(f"Год {year} не является высокосным ")
elif year % 100 != 0:
    print(f"Год {year} является высокосным ")
elif year % 400 != 0:
    print(f"Год {year} не является высокосным ")
else:
    print(f"Год {year} является высокосным ")
