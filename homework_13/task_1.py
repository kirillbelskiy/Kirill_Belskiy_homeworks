import pandas
import csv

data = [
    ("Название", "Автор", "Год издания", "Жанр", "Цена"),
    ["Мастер и Маргарита", "Михаил Булгаков", "1967", "Фэнтези", "500"],
    ["Преступление и наказание", "Фёдор Достоевский", "1866", "Классика", "400"],
    ["1984", "Джордж Оруэлл", "1949", "Научная фантастика", "350"],
    ["Тень горы", "Грегори Дэвид Робертс", "2007", "Триллер", "600"]
]

with open("books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

def load_books(file_path):
    books = []
    with open("books.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Цена'] = int(row['Цена'])
            books.append(row)
    return books

def total_price(books):
    total = 0
    for book in books:
        total += book['Цена']
    return total

def books_by_genre(books, genre):
    books_genre = []
    for book in books:
        if book['Жанр'] == genre:
            books_genre.append((book['Название'], book['Автор']))
    return books_genre

books = load_books("books.csv")
print("Общая стоимость всех книг: ", total_price(books))
genre = "Фэнтези"
print(f"Книги жанра {genre}:")
for title, author in books_by_genre(books, genre):
    print(f"Название: {title}, Автор: {author}")
