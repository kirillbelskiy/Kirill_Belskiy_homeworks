dna = input("Введите ДНК: ")
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
dna_list = list(dna)
for i in range(len(dna_list)):
    dna_list[i] = complement[dna_list[i]]
complement_dna = ''.join(dna_list)
print("Дополнительная сторона ДНК:", complement_dna)
