def analyze_input(input_data):
    if isinstance(input_data, tuple):
        word_lengths = []
        for word in input_data:
            word_lengths.append(len(word))
        return word_lengths
    elif isinstance(input_data, list):
        letters, numbers = 0, 0
        for item in input_data:
            if isinstance(item, str):
                letters += 1
            elif isinstance(item, (int, float)):
                numbers += 1
        return letters, numbers
    elif isinstance(input_data, (int, float)):
        odd_digits = 0
        for digit in str(abs(input_data)):
            if int(digit) % 2 != 0:
                odd_digits += 1
        return odd_digits
    elif isinstance(input_data, str):
        return len(input_data)
    else:
        return "Неизвестный тип данных"
print(analyze_input(("apple", "banana", "cherry")))
print(analyze_input([1, 2, "three", 4, "five"]))
print(analyze_input(13579))
print(analyze_input("Hello, World!"))
