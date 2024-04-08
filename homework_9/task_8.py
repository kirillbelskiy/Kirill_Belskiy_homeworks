a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = []
for i in range(len(a)):
    is_common = False
    for j in range(len(b)):
        if a[i] == b[j]:
            is_common = True
            break
    if is_common:
        is_duplicate = False
        for k in range(len(common_elements)):
            if a[i] == common_elements[k]:
                is_duplicate = True
                break
        if not is_duplicate:
            common_elements.append(a[i])
print(common_elements)
