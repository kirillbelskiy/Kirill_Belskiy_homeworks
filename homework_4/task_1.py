lst = [15, 48, 'hello', 6, 19, 'world']

for i in range(len(lst)):
    item = lst[i]
    if isinstance(item, int):
        if item % 2 == 0:
            sum_of_digits = 0
            while item:
                sum_of_digits += item % 10
                item //= 10
            item = lst[i]
            print(f'Сумма цифр числа {item}: {sum_of_digits}')
        else:
            lst[i] = 1
    elif isinstance(item, str):
        vowels = 'aeiou'
        word = item.lower()
        vowels_count = 0
        consonants_count = 0
        for letter in word:
            if letter in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        print(f'Количество гласных и согласных в слове "{item}": {vowels_count}, {consonants_count}')

print('Обновленный список:', lst)
