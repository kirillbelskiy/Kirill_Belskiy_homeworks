a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]

c = a + b

c.insert(2, 6)

new_c = []
for i in c:
    if not isinstance(i, str):
        new_c.append(i)
c = new_c

count = 0
for i in c:
    count += 1

print('Обновленный список:', c)
print('Количество элементов в списке:', count)
