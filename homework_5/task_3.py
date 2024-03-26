distance = 1
total_distance = 1
days = 1

while total_distance < 10:
    distance *= 1.1
    total_distance += distance
    days += 1

print(f"Васе понадобится {days} дней, чтобы пробежать в сумме хотя бы 10 км.")
