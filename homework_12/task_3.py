def count_lines_and_chars(task_3):
    with open(task_3, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    char_counts = [len(line) for line in lines]

    return line_count, char_counts

line_count, char_counts = count_lines_and_chars('task_3.txt')
print(f"Количество строк: {line_count}")
print(f"Количество символов в каждой строке: {char_counts}")

