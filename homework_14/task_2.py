class Student:
    def __init__(self, name, money):
       self.name = name
       self.money = money

students = [
    Student("Иван", 1000),
    Student("Мария", 1500),
    Student("Алексей", 1200),
    Student("Наталья", 1800),
]

for student in students:
    print(f"Студент {student.name} имеет {student.money} денег.")
