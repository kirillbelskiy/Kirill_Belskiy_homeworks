list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, 4, 0, 23, 6, 34]

for lst in (list1, list2, list3):
    sorted_lst = sorted(lst)
    second_smallest = sorted_lst[1]
    print(f'Второе наименьшее значение в списке: {second_smallest}')
