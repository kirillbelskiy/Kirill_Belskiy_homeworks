def write_and_read_user_input(filename):
    with open(filename, 'w') as file:
        while True:
            user_input = input("Введите данные (или оставьте строку пустой для завершения): ")
            if user_input == "":
                break
            file.write(user_input + '\n')
    print("Запись в файл завершена. Теперь начинаем чтение из файла.")
    with open(filename, 'r') as file:
        print(file.read())

write_and_read_user_input('task_2.txt')

