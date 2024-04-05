dna = input("Введите строку: ")
dna = dna.lower()
count_gc = dna.count('g') + dna.count('c')
percentage_gc = (count_gc / len(dna)) * 100
print("Процентное содержание символов G и C:", percentage_gc)
