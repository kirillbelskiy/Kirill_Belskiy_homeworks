students_grades = {'Алексей': 8, 'Мария': 9, 'Иван': 7, 'Ольга': 3, 'Сергей': 10}

total_grade = 0
for i in students_grades.values():
    total_grade += i
average_grade = total_grade / len(students_grades)

print(f'Средняя оценка по математике для всех студентов: {average_grade}')
