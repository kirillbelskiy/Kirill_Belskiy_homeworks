from datetime import date

class Person:
    def __init__(self, last_name, birth_date):
        self.last_name = last_name
        self.birth_date = birth_date

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today < date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def print_info(self):
        print(f"Фамилия: {self.last_name}\n Возраст: {self.calculate_age()} лет")

class Applicant(Person):
    def __init__(self, last_name, birth_date, faculty):
        super().__init__(last_name, birth_date)
        self.faculty = faculty

    def print_info(self):
        super().print_info()
        print(f"Факультет: {self.faculty}")

class Student(Person):
    def __init__(self, last_name, birth_date, faculty, course):
        super().__init__(last_name, birth_date)
        self.faculty = faculty
        self.course = course

    def print_info(self):
        super().print_info()
        print(f"Факультет: {self.faculty}\n Курс: {self.course}")

class Teacher(Person):
    def __init__(self, last_name, birth_date, faculty, position, experience_years):
        super().__init__(last_name, birth_date)
        self.faculty = faculty
        self.position = position
        self.experience_years = experience_years

    def print_info(self):
        super().print_info()
        print(f"Факультет: {self.faculty}\n Должность: {self.position} \nСтаж: {self.experience_years} лет")

people = [
    Applicant("Иванов", date(1995, 5, 10), "Инженерный"),
    Student("Петров", date(2000, 8, 20), "Экономический", 3),
    Teacher("Сидоров", date(1980, 3, 15), "Медицинский", "Профессор", 15)
]

for person in people:
    person.print_info()

min_age = 25
max_age = 40
filtered_people = [person for person in people if min_age <= person.calculate_age() <= max_age]
print("\nПерсоны в заданном возрастном диапазоне:")
for person in filtered_people:
    person.print_info()
