class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

student1 = Student()
student2 = Student("Maria", 20, "11B")
student3 = Student("Alex", 19, "12C")
student4 = Student("Elena", 21, "13D")
student5 = Student("Max", 22, "14E")

student1.setNameAge("John", 23)
student2.setGroupNumber("15F")

print(f"Студент 1: {student1.getName()}, возраст {student1.getAge()}, группа {student1.getGroupNumber()}")
print(f"Студент 2: {student2.getName()}, возраст {student2.getAge()}, группа {student2.getGroupNumber()}")
print(f"Студент 3: {student3.getName()}, возраст {student3.getAge()}, группа {student3.getGroupNumber()}")
print(f"Студент 4: {student4.getName()}, возраст {student4.getAge()}, группа {student4.getGroupNumber()}")
print(f"Студент 5: {student5.getName()}, возраст {student5.getAge()}, группа {student5.getGroupNumber()}")
