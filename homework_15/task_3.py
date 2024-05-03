class Fruit:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

class Orange(Fruit):
    def clear(self):
        print(f"{self.name} очищен")

class Apple(Fruit):
    def cut(self):
        print(f"{self.name} порезан")

class Mandarin(Fruit):
    def clear(self):
        print(f"{self.name} очищен")

class Banana(Orange):
    def __init__(self, sort, vitamins, price, name, kaliy):
        super().__init__(sort, vitamins, price, name)
        self.kaliy = kaliy

orange = Orange("сорт1", ["A", "B", "C"], 100, "апельсин")
apple = Apple("сорт2", ["D", "E", "B2"], 120, "яблоко")
mandarin = Mandarin("сорт3", ["B12", "A", "C"], 80, "мандарин")
banana = Banana("сорт4", ["D", "E", "B2"], 150, "банан", 450)

orange.clear()
apple.cut()
mandarin.clear()
banana.clear()
print(f"Количество калия в банане: {banana.kaliy}")
