m = int(input("Введите 1-ое число:"))
n = int(input("Введите 2-ое число:"))

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
