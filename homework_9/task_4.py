a = {1:10, 2:20, 3:30}
result = []
for key in a.keys():
    for value in a.values():
        if a[key] == value:
            result.append(key * value)
print(result)
