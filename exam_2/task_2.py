class Tomato:
    states = ["Отсутствует", "Цветение", "Зеленый", "Красный"]

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        current_state_index = self.states.index(self._state)
        next_state_index = (current_state_index + 1) % len(self.states)
        self._state = self.states[next_state_index]

    def is_ripe(self):
        return self._state == self.states[-1]


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name}, подождите, пока все томаты дозреют.")

    @staticmethod
    def knowledge_base():
        print("Садоводство: как вырастить вкусные помидоры и собрать урожай.")


Gardener.knowledge_base()

tomato_bush = TomatoBush(3)

gardener_anna = Gardener("Анна", tomato_bush)

gardener_anna.work()
gardener_anna.work()

if tomato_bush.all_are_ripe():
    print("Все помидоры созрели!")
else:
    print("Еще не все помидоры дозрели.")

gardener_anna.harvest()

gardener_petr = Gardener("Петр", tomato_bush)

gardener_petr.work()

if tomato_bush.all_are_ripe():
    print("Все помидоры созрели!")
else:
    print("Еще не все помидоры дозрели.")

gardener_petr.harvest()
