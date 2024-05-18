def get_coordinates():
    x = int(input("Введите номер столбца клетки (от 1 до 8): "))
    y = int(input("Введите номер строки клетки (от 1 до 8): "))
    return x, y

def can_knight_reach(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx == 1 and dy == 2 or dx == 2 and dy == 1

def can_rook_reach(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

def can_queen_reach(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or x1 - x2 == y1 - y2

def can_bishop_reach(x1, y1, x2, y2):
    return x1 - x2 == y1 - y2

def can_king_reach(x1, y1, x2, y2):
    return x1 - x2 <= 1 and y1 - y2 <= 1

print("Выберите фигуру (конь, ладья, ферзь, слон или король):")
figure = input().lower()

print("Введите координаты первой клетки:")
x1, y1 = get_coordinates()

print("Введите координаты второй клетки:")
x2, y2 = get_coordinates()

if figure == "конь":
    if can_knight_reach(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
elif figure == "ладья":
    if can_rook_reach(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
elif figure == "ферзь":
    if can_queen_reach(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
elif figure == "слон":
    if can_bishop_reach(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
elif figure == "король":
    if can_king_reach(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")
else:
    print("Неверно указана фигура. Пожалуйста, выберите из списка: конь, ладья, ферзь, слон или король.")
