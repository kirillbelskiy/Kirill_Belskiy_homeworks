class Singleton:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = object.__new__(self)
        return self._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
