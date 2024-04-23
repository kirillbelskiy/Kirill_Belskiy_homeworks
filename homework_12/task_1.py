def sort_file_content(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    numbers = []
    words = []
    for line in lines:
        line = line.strip()
        if line.isdigit():
            numbers.append(int(line))
        else:
            words.append(line)
    numbers.sort()
    words.sort(key=len)
    return numbers + words

print(sort_file_content('task_1.txt'))

