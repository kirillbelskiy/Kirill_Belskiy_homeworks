numbers = [1, 5, 2, 4, 1, 5, 2, 3, 5]
max_value = numbers[0]
max_index = 0
for i in range(1, len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i
print("Наибольшее значение:", max_value)
print("Индекс наибольшего значения:", max_index)
