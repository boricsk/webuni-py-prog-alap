
from abc import ABC, abstractmethod

class Testek(ABC):

    def felszin(self):
        return self._felszin
    
    
    def terfogat(self):
        return self._terfogat


class Teglatest(Testek):
    def __init__(self, a, b, c) -> None:
        self._terfogat = a * b * c
        self._felszin = 2 * (a * b + a * c + b * c)
    

class Kocka(Teglatest):
    def __init__(self, a) -> None:
        super().__init__(a, a, a)

class Gomb(Testek):
    PI = 3.1415927
    def __init__(self, r) -> None:
        self._felszin = 4 * r ** 2 * Gomb.PI
        self._terfogat = (4 * r ** 2 * Gomb.PI) / 3
    
    
teglatest = Teglatest(3, 4, 5)
print(teglatest.felszin())
print(teglatest.terfogat())


kocka = Kocka(3)

print(kocka.felszin())
print(kocka.terfogat())

gomb = Gomb(3)

print(gomb.felszin())
print(gomb.terfogat())
