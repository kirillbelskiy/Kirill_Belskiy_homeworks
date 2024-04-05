strings = ["hello my friend", "my name is", "house", "cat", "dog"]
new_list = []
for i in strings:
    if ' ' in i:
        new_list.append(i)
print(new_list)
