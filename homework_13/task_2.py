import csv

def save_dict_to_csv(data_list, filename):
    fieldnames = data_list[0].keys()
    # fieldnames - определяет заголовки для столбцов CSV файлах.
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)

data = [
    {"name": "Петя", "age": 30},
    {"name": "Миша", "age": 25}
]
save_dict_to_csv(data, "data.csv")
