set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1 == set2:
    print("Множества равны")
elif set1.issubset(set2):
    print("Множество 1 состоит из множества 2")
elif set2.issubset(set1):
    print("Множество 2 состоит из множества 1")
elif set1 & set2:
    print("Множества пересекаются:", set1 & set2)
else:
    print("Множества не пересекаются")
