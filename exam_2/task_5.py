class Wizard:
    def __init__(self, name, rating, apparent_age):
        self.name = name
        self.rating = max(1, min(100, rating))
        self.apparent_age = max(18, apparent_age)

    def change_rating(self, value):
        self.rating = max(1, min(100, self.rating + value))
        if value > 0:
            self.apparent_age = max(18, self.apparent_age - value // 10)
        else:
            self.apparent_age += value // 10

    def __iadd__(self, string):
        self.rating += len(string)
        self.apparent_age -= len(string) // 10
        return self

    def __call__(self, argument):
        return (argument - self.apparent_age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.apparent_age} years old"

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.apparent_age != other.apparent_age:
            return self.apparent_age < other.apparent_age
        else:
            return self.name < other.name

    def __gt__(self, other):
        if self.rating != other.rating:
            return self.rating > other.rating
        elif self.apparent_age != other.apparent_age:
            return self.apparent_age > other.apparent_age
        else:
            return self.name > other.name

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __eq__(self, other):
        return self.rating == other.rating and self.apparent_age == other.apparent_age and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


gandalf = Wizard("Gandalf", 90, 60)
merlin = Wizard("Merlin", 85, 45)

print(gandalf)
print(merlin)

gandalf.change_rating(15)
merlin += "Abracadabra"

print(f"Gandalf's new rating: {gandalf.rating}")
print(f"Merlin's new age: {merlin.apparent_age}")

result = gandalf(70)
print(f"Result of calling Gandalf with argument 70: {result}")

print(f"Comparison: Gandalf > Merlin: {gandalf > merlin}")
