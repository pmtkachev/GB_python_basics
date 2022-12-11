from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expenditure(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def expenditure(self):
        return round((self.v / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, name, h):
        super(Suit, self).__init__(name)
        self.h = h

    @property
    def expenditure(self):
        return self.h * 2 + 0.3


c = Coat('пальто', 46)
s = Suit('костюм', 170)
print(c.expenditure)
print(s.expenditure)
# Общий подсчет расхода ткани
print(c.expenditure + s.expenditure)
