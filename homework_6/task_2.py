numbers = [1, -2, 3, -2, -5, 6, 5]
for i in range(1, len(numbers)):
    if (numbers[i] > 0 and numbers[i-1] > 0) or (numbers[i] < 0 and numbers[i-1] < 0):
        print(numbers[i-1], numbers[i])
        break
