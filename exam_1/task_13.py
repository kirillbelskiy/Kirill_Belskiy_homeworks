strings = ['1', '2', '3', '4', 'hello', '', 'good', '', '', '5', '6', '7']
new_strings = []
for i in strings:
    if i != '':
        new_strings.append(i)
strings = new_strings
print(strings)
