numbers = [1, 2, 3, 2, 5, 6, 5]
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])

