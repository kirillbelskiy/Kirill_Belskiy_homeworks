numbers = [1, 3, 2, -99, 1, 5, 2, 3, 99]
min_value = numbers[0]
max_value = numbers[0]
min_index = 0
max_index = 0

for i in range(1, len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_index = i
    elif numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

a = numbers[min_index]
numbers[min_index] = numbers[max_index]
numbers[max_index] = a
print(numbers)

