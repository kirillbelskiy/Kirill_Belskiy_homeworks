S  = input("Введите строку (В строке должно быть хотя бы два символа) ")
i = len(S)
while i < 2:
    print("Неверный ввод, повторите попытку")
    S = input("Введите строку (В строке должно быть хотя бы два символа) ")
    i = len(S)
print(S[2::3])
print(S[0] + S[-1])
print(S.upper())
print(S[::-1])
if S.isdigit():
    print(True)
else:
    print(False)
