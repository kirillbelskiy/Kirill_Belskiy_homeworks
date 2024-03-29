a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

unique_a = []
unique_b = []

for i in a:
    if i not in unique_a:
        unique_a.append(i)

for i in b:
    if i not in unique_b:
        unique_b.append(i)

common_elements = []

for item in unique_a:
    if item in unique_b:
        common_elements.append(item)

print(f'Общие элементы для двух списков: {common_elements}')