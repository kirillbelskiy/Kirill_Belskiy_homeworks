long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и','и', 'i', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
f = {}
for letter in long_word:
    if letter not in f:
        f[letter] = long_word.count(letter)
print(f)
