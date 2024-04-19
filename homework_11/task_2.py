def more_than_five(lst):
    result = []
    for i in lst:
        if abs(i) > 5:
            result.append(i)
    return result

print(more_than_five([1, -10, 2, 6, -7, 12]))
