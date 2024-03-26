import random

attempts = 5
while attempts > 0:
    number = random.randint(1, 10)
    color = random.randint(1, 2)
    if color == 1:
        color = 'красный'
    else:
        color = 'черный'

    guess_number = int(input("Введите номер (от 1 до 10): "))
    guess_color = input("Введите цвет ('красный' или 'черный'): ")

    if guess_number == number and guess_color == color:
        print("Поздравляем, вы угадали!")
        break
    else:
        print(f"Неправильно. Правильная комбинация: {number} {color}")
        attempts -= 1

if attempts == 0:
    print("К сожалению, вы не угадали за 5 попыток.")
