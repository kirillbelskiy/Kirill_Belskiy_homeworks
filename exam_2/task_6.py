class Worker:
    def __init__(self, name, position, experience_years):
        self.name = name
        self.position = position
        self.experience_years = experience_years

    def print_info(self):
        if self.experience_years == 1:
            years_word = "год"
        elif 2 <= self.experience_years <= 4:
            years_word = "года"
        else:
            years_word = "лет"

        print(f"Имя: {self.name} Должность: {self.position} Стаж: {self.experience_years} {years_word}")


worker1 = Worker("Алексей", "Программист", 17)
worker2 = Worker("Анна", "Маркетолог", 2)
worker3 = Worker("Дмитрий", "Аналитик", 1)

worker1.print_info()
worker2.print_info()
worker3.print_info()
