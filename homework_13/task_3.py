import csv
import time

with open("rows_300.csv", "w", newline="") as file:
    fieldnames = ["№", "Секунда", "Микросекунда"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, 301):
        now = time.time()
        seconds = int(now)
        microseconds = int((now - seconds) * 1 * 10 ** 6)
        writer.writerow({"№": i, "Секунда": seconds % 60, "Микросекунда": microseconds})
        time.sleep(0.01)
