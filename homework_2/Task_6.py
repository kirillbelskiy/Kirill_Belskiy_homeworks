name = input("Введите строку: ")
words = name.split()
words = words[::-1]
reversed_name = ' '.join(words)
print(reversed_name)
