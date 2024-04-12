numbers = [1, 23, 43, 22, -2]
def find_max(numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
print(find_max(numbers))