class Student:
    def __init__(self, surname_and_initials, group_number, number):
        self.surname_and_initials = surname_and_initials
        self.group_number = group_number
        self.number = number


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_excellent_students(self):
        for student in self.students:
            if all(mark == 5 or mark == 6 for mark in student.performance):
                print(f"Фамилия и инициалы: {student.surname_and_initials}, Номер группы: {student.group_number}")

    def print_students_of_group(self, group_number):
        for student in self.students:
            if student.group_number == group_number:
                print(f"Фамилия и инициалы: {student.surname_and_initials}")

    def print_automat_students(self):
        for student in self.students:
            if sum(student.number) / len(student.number) >= 7:
                print(f"Фамилия и инициалы: {student.surname_and_initials}")


school = School()

while True:
    print("Выберите действие:")
    print("1 - Добавить студента")
    print("2 - Вывести хорошистов")
    print("3 - Вывести студентов определенной группы")
    print("4 - Вывести студентов, претендующих на автомат")
    print("5 - Завершить программу")
    action = input()

    if action == "1":
        surname_and_initials = input("Введите фамилию и инициалы студента: ")
        group_number = input("Введите номер группы студента: ")

        print("Введите оценки студента через пробел: ")
        number_input = input()
        number_list = number_input.split()
        number = [int(mark) for mark in number_list]

        student = Student(surname_and_initials, group_number, number)

        school.add_student(student)
    elif action == "2":
        school.print_excellent_students()
    elif action == "3":
        group_number = input("Введите номер группы, чтобы увидеть список студентов: ")
        school.print_students_of_group(group_number)
    elif action == "4":
        school.print_automat_students()
    elif action == "5":
        break
    else:
        print("Неверный ввод. Пожалуйста, попробуйте еще раз.")

