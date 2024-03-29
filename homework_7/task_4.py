name = input("Введите строку: ")
name = name.lower()
count_gc = name.count('g') + name.count('c')
length_name = len(name)
percentage = (count_gc / length_name) * 100
print(f'Процентное содержание символов G и C: {percentage}%')
