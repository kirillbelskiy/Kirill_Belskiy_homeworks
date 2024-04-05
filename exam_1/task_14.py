text = input("Введите текст: ")
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
most_common_word = ''
max_count = 0
for word, count in word_counts.items():
    if count > max_count:
        most_common_word = word
        max_count = count
longest_word = ''
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)
